from transformers import pipeline, GPT2Tokenizer, GPT2LMHeadModel

def main():
    # Load GPT-2 tokenizer and model
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    model = GPT2LMHeadModel.from_pretrained("gpt2")

    # Build a text generation pipeline
    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

    # Test generation
    prompt = "Generate a unique domain name for an organic coffee shop:"
    result = generator(prompt, max_length=20, num_return_sequences=1)

    print("Sample generation:")
    print(result)

if __name__ == "__main__":
    main()
