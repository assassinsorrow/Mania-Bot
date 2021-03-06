from .CreateAppdataDir import CreateAppdataDir

# generates base folder
CreateAppdataDir()
from .CreateConfigFiles import CreateConfigFiles
from .CreateConfigFolder import CreateConfigFolder
from .CreatePluginFolder import CreatePluginFolder
from .DefualtConfigs import (
    Defualt_Config_Osu4K,
    Defualt_Config_Quaver4K,
    Defualt_Settings,
)
from .Paths import AppDataConfigDir, AppDataDir, PluginsDir
from .LoadConfig import LoadConfig
from .LoadSettings import LoadSettings
