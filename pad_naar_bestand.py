
import os

def abs_to_rel_path(bestandsnaam_met_extensie):
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = bestandsnaam_met_extensie
    link_to_file = os.path.join(script_dir, rel_path)
    return link_to_file
  

