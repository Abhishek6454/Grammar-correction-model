from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

class GrammarCorrector:
    def __init__(self):
        # Load the fine-tuned model and tokenizer
        self.model = T5ForConditionalGeneration.from_pretrained("grammar_model/t5-grammar-correction-model")
        self.tokenizer = T5Tokenizer.from_pretrained("grammar_model/t5-grammar-correction-model")

    def correct_grammar(self, text):
        input_text = "correct: " + text
        input_ids = self.tokenizer(input_text, return_tensors="pt").input_ids

        # Generate output
        with torch.no_grad():
            output_ids = self.model.generate(input_ids, max_length=128, num_beams=5, early_stopping=True)

        corrected_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return corrected_text

