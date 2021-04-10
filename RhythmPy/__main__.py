# imports
try:
    # fmt: off
    import platform
    # Starts Logger
    try:
        from Core import FileManager
        from Core.Logger import Logger
        # creates appdata dir
        FileManager.CreateAppdataDir()
        logger = Logger()
        # creates log folder
        logger.CreateLogFolder()
        logger = logger.StartLogger(name=__name__)
    except (ImportError, ModuleNotFoundError) as e:
        print("failed to start logger\n", e)
        input()
        exit()

    # Splash Screen
    try:
        from Core.Gui import SplashScreen
        # starts splash screen
        splash = SplashScreen()
        splash.Start()
    except (ImportError, ModuleNotFoundError):
        logger.exception("failed to start splash screen\n")
        splash = None

    # creates needed files
    try:
        FileManager.CreateConfigFolder()
        FileManager.CreateConfigFiles()
        FileManager.CreatePluginFolder()
    except (ImportError, ModuleNotFoundError):
        logger.exception("Failed to create needed files\n")

    # imports the actual bot
    try:
        from Core import (
            FirstRun,
            Gui,
            Cli,
            CloseGlobal,
        )
    except (ImportError, ModuleNotFoundError):
        logger.exception("failed to import the bot\n")
        exit()
    # fmt: on
except Exception as e:
    print(e)
    input()
    exit()

if __name__ == "__main__":
    # gets current running system
    platform = platform.system()
    ConfigFile = FileManager.LoadSettings()

    # first run stuff
    try:
        if ConfigFile["FirstRun"] in [True, "True", "true"]:
            FirstRun().Run()
        else:
            logger.info("has been run before carrying on")
    except Exception:
        logger.warning("failed to apply skins\n")

    # starts the bot
    try:
        splash.Stop()
        if ConfigFile["CliMode"] in [True, "True", "true"]:
            Cli.Run()
        else:
            Gui.Run()
    except Exception:
        Gui.Run()
    except Exception:
        logger.exception("failed to start RhythmPy\n")
