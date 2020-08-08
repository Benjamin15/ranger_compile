import ctypes, sys

from pathlib import Path
from panelDetails import set_detail_panel
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def install():
    if is_admin():
        print('je suis admin')
        try: # Works only with windows
            import winreg

            path_main = Path(Path.cwd(), 'ranger', 'main.cpython-38.pyc')
            path_historic = Path(Path.cwd(), 'app', 'view', 'operations.cpython-38.pyc')
            path_rules = Path(Path.cwd(), 'app', 'view', 'rules.cpython-38.pyc')
            
            # TODO add icon winreg.SetValue(key_ranger, 'icon', path_icon)

            key_ranger = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'DIRECTORY\\Background\\shell\\ranger')
            key_command = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'DIRECTORY\\Background\\shell\\ranger\\command')
        
            


            key_ranger_historic = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'DIRECTORY\\Background\\shell\\ranger_archive')
            key_command_historic = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'DIRECTORY\\Background\\shell\\ranger_archive\\command')
            
            key_ranger_rules = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'DIRECTORY\\Background\\shell\\ranger_rules')
            key_command_rules = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, 'DIRECTORY\\Background\\shell\\ranger_rules\\command')

            # TODO add icon winreg.SetValue(key_ranger, 'icon', path_icon)
            
            winreg.SetValue(key_command, '', winreg.REG_SZ, f"{sys.executable} {path_main}")
            winreg.CloseKey(key_command)

            winreg.SetValue(key_command_historic, '', winreg.REG_SZ, f"{sys.executable} {path_historic}")
            winreg.CloseKey(key_command_historic)

            winreg.SetValue(key_command_rules, '', winreg.REG_SZ, f"{sys.executable} {path_rules}")
            winreg.CloseKey(key_command_rules)

            # set_detail_panel(".txt")

        except (OSError, ImportError) as e:
            print(e)

    else:
        print('Tu dois te reconnecter en admin')

if __name__ == "__main__":
    install()