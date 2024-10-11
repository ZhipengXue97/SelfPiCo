# Extracted from ./data/repos/scrapy/scrapy/cmdline.py
if argv is None:
    argv = sys.argv

if settings is None:
    settings = get_project_settings()
    # set EDITOR from environment if available
    try:
        editor = os.environ["EDITOR"]
    except KeyError:
        pass
    else:
        settings["EDITOR"] = editor

inproject = inside_project()
cmds = _get_commands_dict(settings, inproject)
cmdname = _pop_command_name(argv)
if not cmdname:
    _print_commands(settings, inproject)
    sys.exit(0)
elif cmdname not in cmds:
    _print_unknown_command(settings, cmdname, inproject)
    sys.exit(2)

cmd = cmds[cmdname]
parser = ScrapyArgumentParser(
    formatter_class=ScrapyHelpFormatter,
    usage=f"scrapy {cmdname} {cmd.syntax()}",
    conflict_handler="resolve",
    description=cmd.long_desc(),
)
settings.setdict(cmd.default_settings, priority="command")
cmd.settings = settings
cmd.add_options(parser)
opts, args = parser.parse_known_args(args=argv[1:])
_run_print_help(parser, cmd.process_options, args, opts)

cmd.crawler_process = CrawlerProcess(settings)
_run_print_help(parser, _run_command, cmd, args, opts)
sys.exit(cmd.exitcode)
