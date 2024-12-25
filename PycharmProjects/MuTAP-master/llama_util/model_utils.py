# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the GNU General Public License version 3.

#from peft import PeftModel
from transformers import LlamaForCausalLM

# Function to load the main model for text generation
def load_model(model_name, quantization,access_token):
    model = LlamaForCausalLM.from_pretrained(
        model_name,
        return_dict=True,
        load_in_8bit=quantization,
        device_map="auto",
        low_cpu_mem_usage=True,
        use_auth_token= access_token,
    )
    return model


# Function to load the PeftModel for performance optimization
# def load_peft_model(model, peft_model):
#     peft_model = PeftModel.from_pretrained(model, peft_model)
#     return peft_model