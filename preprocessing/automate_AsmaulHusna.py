import os
import pandas as pd

def do_preprocessing(input_path, output_path):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"File data mentah tidak ditemukan di: {input_path}")
        
    df = pd.read_csv(input_path)
    
    df_clean = df.dropna(subset=['text_clean', 'label'])
    df_clean = df_clean[['text_clean', 'label']]
    df_clean['text_clean'] = df_clean['text_clean'].astype(str)
    df_clean['label'] = df_clean['label'].astype(int)
    
    df_clean.to_csv(output_path, index=False)
    print(f"Sukses! Data bersih disimpan ke {output_path}")
    return df_clean

if __name__ == "__main__":
    INPUT_FILE = os.path.join("..", "Getcontact.csv")
    OUTPUT_FILE = "getcontact_preprocessing.csv"
    
    do_preprocessing(INPUT_FILE, OUTPUT_FILE)