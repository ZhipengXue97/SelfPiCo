# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/python/tfr_gen.py
out_type = self._get_inferred_type(node)
vals = []
tys = []
for elt in node.elts:
    val, ty = self.visit(elt)
    ty = self._get_inferred_type(elt, ty)
    if ty in _ATTRIBUTE_TYPES and out_type == TFRTypes.TENSOR_LIST:
        # This list is a tensor list, then cast all the input values to tensors.
        val, ty = self._value_to_tensor(val, ty, node)
    else:
        # We shouldn't use index type to build the list because list will be use
        # as attribute.
        val, ty = self._index_to_I64(val, ty)
    vals.append(val)
    tys.append(str(ty))

list_val = self._ssa_name('list')
self.emit('\n{} = "tfr.build_list"({})'.format(list_val, ', '.join(vals)))
self._emit_with_loc(' : ({}) -> {}'.format(', '.join(tys), out_type), node)
exit((list_val, out_type))
