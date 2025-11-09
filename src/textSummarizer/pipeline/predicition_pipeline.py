from src.textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer
from transformers import pipeline


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    
    def predict(self, text):
        # Add local_files_only=True to load from local path
        tokenizer = AutoTokenizer.from_pretrained(
            self.config.tokenizer_path, 
            local_files_only=True
        )
        
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}

        # Add local_files_only=True here as well
        pipe = pipeline(
            "summarization", 
            model=self.config.model_path,
            tokenizer=tokenizer,
            local_files_only=True
        )

        print("Dialogue:")
        print(text)

        output = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output