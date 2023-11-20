import oom_markdown
import os

#process
#  locations set in working_parts.ods 
#  export to working_parts.csv
#  put components on the right side of the board
#  run this script

def main(**kwargs):
    make_readme(**kwargs)
    
    

def make_readme(**kwargs):
    os.system("generate_resolution.bat")
    oom_markdown.generate_readme_project(**kwargs)
    
    
#take component positions from working_parts.csv and place them in working.kicad_pcb





if __name__ == '__main__':
    main()