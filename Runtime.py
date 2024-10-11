import atexit
import sys
import time
import json
import os
from .Hyperparams import Hyperparams as params
from .TraceWriter import TraceWriter
from .RuntimeStats import RuntimeStats
from .Logging import logger
from .predictor.CodeLLama.ValuePredictor import CodeLLamaValuePredictor
from .predictor.CodeLLama.TypePredictor import CodeLLamaTypePredictor
from .Util import exec_predict, store_memory, load_memory, remove_comments


logger.info("Runtime starting")

# ------- begin: select mode -----
# mode = "RECORD"    # record values and write into a trace file
mode = "PREDICT"   # predict and inject values if missing in exeuction
# mode = "REPLAY"  # replay a previously recorded trace (mostly for testing)
# ------- end: select mode -------

file_type = "SOURCE"
# file_type = "TESTE"

if mode == "RECORD":
    trace = TraceWriter()
    atexit.register(lambda: trace.write_to_file())
    runtime_stats = None
elif mode == "PREDICT":
    # predictor = AsIs()
    # predictor = NaiveValuePredictor()
    # predictor = RandomPredictor()
    # predictor = FrequencyValuePredictor("values_frequencies.json")
    # predictor = NeuralValuePredictor()

    runtime_stats = RuntimeStats()
    atexit.register(runtime_stats.print)
    valuepredictor = CodeLLamaValuePredictor(runtime_stats)
    typepredictor = CodeLLamaTypePredictor(runtime_stats)
    start_time = time.time()
    valuepredictor_name = valuepredictor.__class__.__name__

    # for running experiments
    if file_type == "SOURCE":
        file = sys.argv[0]
    elif file_type == "TESTE":
        file = sys.argv[1]
        
    atexit.register(runtime_stats.save, file, valuepredictor_name, start_time)
elif mode == "REPLAY":
    with open("trace.out", "r") as file:
        trace = file.readlines()
    next_trace_idx = 0
    runtime_stats = None

logger.info(f"### LExecutor running in {mode} mode ###")

# map kind+name to predicted value to ensure consistent predictions for the same name
# memorypath = params.tmp_dir + "memory.json"
env_value = {}
# if os.path.exists(memorypath):
#     valuepredictor.env = load_memory(memorypath)
# for key in valuepredictor.env:
#     name = key.split('#')[-1]
#     e = valuepredictor.env[key]
#     env_value[key] = exec_predict(name, e)




def _n_(iid, name, lambada):

    if params.verbose:
        logger.info(f"\nAt iid={iid}, looking up name '{name}'")

    if runtime_stats is not None:
        runtime_stats.total_uses += 1
        runtime_stats.cover_iid(iid)
    if name == "self":
        name = "my_obj"

    perform_fct = lambada

    def record_fct(v):
        trace.append_name(iid, name, v)

    def predict_value(e):
        e = str(e)
        key = f"name#{name}"
        if key in env_value:
            return env_value[key]
        else:
            v= valuepredictor.name(iid, name, e)
            env_value[key] = v
            return v
        
    def predict_type():
        key = f"name#{name}"
        if key in env_value:
            return env_value[key]
        else:
            v = typepredictor.name(iid, name)
            env_value[key] = v
            return v
        
    def mode_branch(iid, record_fct, perform_fct, predict_value, predict_type):
        if mode == "RECORD":
            v = perform_fct()
            record_fct(v)
            return v
        elif mode == "PREDICT":
            try:
                v = perform_fct()
                if params.verbose:
                    logger.info("Found/computed/returned regular value")
                return v
            except Exception as e:
                if (type(e) == NameError):
                    if params.verbose:
                        logger.info(
                            f"Catching '{type(e)}' during name valuepredictor instead")
                    # try:
                    #     v= predict_value(e)
                    # except:
                    v= predict_type()
                    runtime_stats.guided_uses += 1
                    return v
                else:
                    if params.verbose:
                        logger.info(
                            f"Exception '{type(e)}' not caught, re-raising")
                    runtime_stats.uncaught_exception(iid, e)
                    # store_memory(memorypath)
                    raise e
        
    return mode_branch(iid, record_fct, perform_fct, predict_value, predict_type)




def _c_(iid, fct, *args, **kwargs):
    if params.verbose:
        logger.info(f"\nAt iid={iid}, calling function {fct}")

    if runtime_stats is not None:
        runtime_stats.total_uses += 1
        runtime_stats.cover_iid(iid)

    def record_fct(v):
        trace.append_call(iid, fct, args, kwargs, v)

    def perform_fct():
        return fct(*args, **kwargs)


    def predict_value(e):
        fct_name = fct.__name__ if hasattr(fct, "__name__") else str(fct)
        if " " in fct_name:  # some fcts that don't have a proper name
            fct_name = fct_name.split(" ")[0]

        e = str(e)
        key = f"call#{fct_name}"
        if key in env_value:
            return env_value[key]
        else:
            v = valuepredictor.call(iid, fct, fct_name, e)
            env_value[key] = v
            return v
        
    def predict_type():
        fct_name = fct.__name__ if hasattr(fct, "__name__") else str(fct)
        if " " in fct_name:  # some fcts that don't have a proper name
            fct_name = fct_name.split(" ")[0]

        key = f"call#{fct_name}"
        if key in env_value:
            return env_value[key]
        else:
            v = typepredictor.call(iid, fct, fct_name, args, kwargs)
            env_value[key] = v
            return v
        
    def mode_branch(iid, record_fct, perform_fct, predict_value, predict_type, fct):  
        if mode == "RECORD":
            v = perform_fct()
            record_fct(v)
            return v
        elif mode == "PREDICT":
            try:
                v = perform_fct()
                if params.verbose:
                    logger.info("Found/computed/returned regular value")
                return v
            except Exception as e:
                if params.verbose:
                    logger.info(
                        f"Catching '{type(e)}' during calling valuepredictor instead")
                # try:
                #     v= predict_value(e)
                # except:
                v= predict_type()
                runtime_stats.guided_uses += 1
                return v

            
    return mode_branch(iid, record_fct, perform_fct, predict_value, predict_type, fct)
        



def _a_(iid, base, attr_name):
    if params.verbose:
        logger.info(f"\nAt iid={iid}, looking up attribute '{attr_name}'")

    if runtime_stats is not None:
        runtime_stats.total_uses += 1
        runtime_stats.cover_iid(iid)

    def record_fct(v):
        trace.append_attribute(iid, base, attr_name, v)

    def predict_value(e):
        message  = str(e)
        start = message.find("'") + 1 
        end = message.find("'", start)
        classname = message[start:end]

        v = valuepredictor.attribute(iid, classname, attr_name, e)
        return v

    def predict_type():
        key = f"attr#{attr_name}"
        if key in env_value:
            return env_value[key]
        else:
            v = typepredictor.attribute(iid, base, attr_name)
            env_value[key] = v
            return v
    

    def perform_fct():
        # return getattr(base, attr_name)
        # unmangle private attributes (code copied from DynaPyt)
        if (attr_name.startswith('__')) and (not attr_name.endswith('__')):
            if type(base).__name__ == 'type':
                parents = [base]
            else:
                parents = [type(base)]
            found = True
            while len(parents) > 0:
                found = True
                cur_par = parents.pop()
                try:
                    cur_name = cur_par.__name__
                    cur_name = cur_name.lstrip('_')
                    return getattr(base, '_'+cur_name+attr_name)
                except AttributeError:
                    found = False
                    parents.extend(list(cur_par.__bases__))
                    continue
                break
            if not found:
                raise AttributeError()
        else:
            return getattr(base, attr_name)
        
    def mode_branch(iid, record_fct, perform_fct, predict_value, predict_type):  
        if mode == "RECORD":
            v = perform_fct()
            record_fct(v)
            return v
        elif mode == 'PREDICT':
            try:
                v = perform_fct()
                if params.verbose:
                    logger.info("Found/computed/returned regular value")
                return v
            except Exception as e:
                    if type(e) == AttributeError:
                        # try:
                        #     v= predict_value(e)
                        # except:
                        v= predict_type()
                        runtime_stats.guided_uses += 1
                        return v
                    else:
                        if params.verbose:
                            logger.info(
                                f"Exception '{type(e)}' not caught, re-raising")
                        runtime_stats.uncaught_exception(iid, e)
                        # store_memory(memorypath)
                        raise e

    return mode_branch(iid, record_fct, perform_fct, predict_value, predict_type)



def _l_(iid):
    if runtime_stats is not None:
        runtime_stats.cover_line(iid)
        runtime_stats.save(file, valuepredictor_name, start_time)

