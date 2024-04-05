import install
from .utils import download_hf, get_base_dir
import time

class HFDownloader:     

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {       
                "repo_id":  ("STRING", {"multiline": False, "default": "ByteDance/SDXL-Lightning"}),
                "filename": ("STRING", {"multiline": False, "default": "sdxl_lightning_2step_lora.safetensors"}),
                "save_dir": ("STRING", {"multiline": False, "default": get_base_dir()}),
            },
            #"optional" : {}
        }
        
    RETURN_TYPES = ()
    #RETURN_NAMES = ()
    FUNCTION     = "download"
    OUTPUT_NODE  = True
    CATEGORY     = "loaders"

    # inputs match input types
    def download(self, repo_id, filename,save_dir):
        print("Dowloading")
        print(f"\t{repo_id}")
        print(f"\t{filename}")
        print(f"\t{save_dir}")
        download_hf(repo_id, filename,save_dir)
        return {}