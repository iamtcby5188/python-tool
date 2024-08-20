import os
import subprocess

_List_Sign_exe = [

    "CubeAgent.exe",
    "CubeAssistant.exe",
    "CubeCredentialProvider.dll",
    "CubeHMI.exe",
    "CubeLicense.exe",
    "CubeLogStash.exe",
    "CubeMobileEngine.exe",
    "CubeRecord.exe",
    "CubeExtensionInstaller.exe", "CubeJavaBridge_x64.dll", "CubeJavaBridge.dll",
    "CubeExtensionInstaller.exe", "CubeRobotNativeMsg.exe",
    "CubeRPA.exe",
    "CubeTray.exe",
    "CubeUiaDispatchor.exe",
    "CubeBus.exe",
    "CubeCenterService.exe", "launch.exe",
    "CubeService.exe", "CubeServiceLaunch.exe"

]

if __name__ == '__main__':
    path: str = r'D:\projects\autopacker\src\CubePlatform\CubePlatformSetup\bin\workspace\app'
    for root, dirs, files in os.walk(path):
        for f in files:
            if f in _List_Sign_exe:
                absPath = os.path.join(root,f)
                print(absPath)
                try:
                    command = ["signtool", "sign", "/tr", "http://timestamp.comodoca.com", "/td", "sha256", "/fd",
                               "sha256", "/a",
                               absPath]
                    print(" ".join(command))
                    # sign_cmd = f'signtool sign /tr http://timestamp.comodoca.com /td sha256 /fd sha256 /a "{path}"'
                    # subprocess.run(command, capture_output=True, text=True, check=True)
                    # Packer._execute_command(sign_cmd, stdout=self.stdout_filepath, stderr=self.stderr_filepath)
                except Exception as err:
                    print(err)
