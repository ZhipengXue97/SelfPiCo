# Extracted from ./data/repos/scrapy/scrapy/commands/__init__.py
"""
        Populate option parse with options available for this command
        """
group = parser.add_argument_group(title="Global Options")
group.add_argument(
    "--logfile", metavar="FILE", help="log file. if omitted stderr will be used"
)
group.add_argument(
    "-L",
    "--loglevel",
    metavar="LEVEL",
    default=None,
    help=f"log level (default: {self.settings['LOG_LEVEL']})",
)
group.add_argument(
    "--nolog", action="store_true", help="disable logging completely"
)
group.add_argument(
    "--profile",
    metavar="FILE",
    default=None,
    help="write python cProfile stats to FILE",
)
group.add_argument("--pidfile", metavar="FILE", help="write process ID to FILE")
group.add_argument(
    "-s",
    "--set",
    action="append",
    default=[],
    metavar="NAME=VALUE",
    help="set/override setting (may be repeated)",
)
group.add_argument("--pdb", action="store_true", help="enable pdb on failure")
