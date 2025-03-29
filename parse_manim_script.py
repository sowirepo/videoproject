import os
import sys

def parse_manim(script_filename):
    with open(script_filename, 'r') as f:
        lines = f.readlines()

    with open(f'./parsed_scripts/parsed_{script_filename}', 'w') as f:
        f.write('trackerdurationvar=1/15\n')
        for line in lines:

            if line == '\n' or len(line.strip()) == 0:
                continue

            if line.strip()[0] == '#':
                continue
            
            if line.startswith('from manim_voiceover'):
                continue

            if line.startswith('class Test'):
                f.write('class Test(MovingCameraScene):\n')
                continue

            if line.find('self.set_speech_service') != -1:
                f.write(line.replace('self.set_speech_service', ''))
                continue

            if line.find('OpenAIService') != -1:
                f.write(line.replace('OpenAIService', 'NOTHING'))
                continue

            if line.find('self.voiceover') != -1:
                f.write(line.replace('with self.voiceover', 'if True:#'))
                continue

            if line.find('self.wait') != -1:
                f.write(line.replace('self.wait', 'pass#'))
                continue
            
            if line.find('tracker.duration') != -1:
                f.write(line.replace('tracker.duration', 'trackerdurationvar)#'))
                continue


            f.write(line)

def main():
    try:
        script_filename = sys.argv[1]
    except IndexError:
        print('Please provide a script to parse.')
        return
    
    if not os.path.exists(script_filename):
        print(f'{script_filename} does not exist.')
        return
    
    if not script_filename.endswith('.py'):
        print('Please provide a python script.')
        return
    
    parse_manim(script_filename)

if __name__ == '__main__':
    main()