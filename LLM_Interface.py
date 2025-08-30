from llama_cpp import Llama
import copy
import json
import re
from datetime import datetime

#import torch


def print_time_difference(startTime, endTime):

    totaleTime = (endTime - startTime).total_seconds()

    minutes = int(totaleTime // 60)
    seconds = int(totaleTime % 60)

    print(f"Elapsed Time: [[{minutes} mins {seconds} sec]]")
    

#Feed the model with an input and display the output
def feedModel(modelInput, llm, writeToFile=False, streamToConsole=True):
    
    modelInput = remove_timestamps(modelInput)
    
    #print("********************>", modelInput)
    
    # output = llm(
        # modelInput,
        # suffix='▌',
        # max_tokens=0,
        # temperature=0.7,
        # echo=False,
        # mirostat_tau=3.5,
        # model="llama2",
        # stream=True,
        # stop='▌'
    # )
    
    output = llm(
        modelInput,
        max_tokens=0,
        echo=False,
        model="Llama3",
        stream=True,
    )
    
    #print(output['choices'])

    #Open the file with the append suffix, so all new data that is added is appended
    reportFile = open("complete.txt", "a")
    
    writeToFile = False
    streamToConsole = True
    
    print("==============================")
    for line in output:
        if streamToConsole:
            print(line['choices'][0]['text'], end="")
            #print(line)
            #print(line, end="")
        if writeToFile:
            reportFile.write(line['choices'][0]['text'])
            #reportFile.write(output)
        #print(line)
    print("\n==============================")
    

    reportFile.close()
    llm.reset()
    
def remove_timestamps(fileData):
    
    #The regex that will identify the time stamps
    pattern = r'\b\d{1,2}:\d{2}\b'
    
    result = re.sub(pattern, '', fileData)
    
    return result

#device = torch.device("cuda")

print("Loading model...")
# llm = Llama(model_path="/mnt/d/Workspaces/Git Local Repo/LLM RAG/models/llama-2_13b_q8.gguf",
            # verbose=False, n_gpu_layers=4, n_threads=2, n_batch=99999, offload_kqv=True, n_ctx=512)
            
#export CUDA_VISIBLE_DEVICES="" - Run this line to disable CUDA devices
#export CUDA_VISIBLE_DEVICES=1,2 - Run this to revert this change
            
llm = Llama(model_path="./models/llama-2-7b.Q8_0.gguf", verbose=True, n_gpu_layers=-1, f16_kv=True,)            
            

print("Model loaded")


running=True

while(running):
    print("Q: ", end="")
    
    userQuestion = input()
    
    startTime = datetime.now()
    if userQuestion.upper() == "EXIT":
        running = False
    
    elif userQuestion.upper() == "READ":
        print("Reading file data...")
        file = open("Prompt_Data.txt", "r")
        fileArray = file.read().split("▌")
        
    
    else:
        modelInput = f"{userQuestion}"
        

    
    if running:
        
        if userQuestion.upper() == "READ":
            
            #clear all data currently in the file
            reportFile = open("complete.txt", "w")
            reportFile.write("")
            reportFile.close()
            for section in fileArray:
                feedModel(f"[{section}]" + ":\n\n Now here's the same message with grammar corrections, spelling corrections and punctuation: \n\n", llm, writeToFile=True)
        else:
            #print("====>: ", modelInput)
            output = feedModel(f"{userQuestion}", llm)

    else:
        print("Exiting...")
        
    
    completeTime = datetime.now()
    print_time_difference(startTime, completeTime)




# for line in output:
#     CompletionFragment = copy.deepcopy(line)
#     print(CompletionFragment['choices'])
