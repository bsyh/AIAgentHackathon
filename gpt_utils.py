import os
import openai

default_prompt = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Provide a recipe for spaghetti bolognese"}
  ]

default_schema = {
  "type": "object",
  "properties": {
    "ingredients": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": { "type": "string" },
          "unit": { 
            "type": "string",
            "enum": ["grams", "ml", "cups", "pieces", "teaspoons"]
          },
          "amount": { "type": "number" }
        },
        "required": ["name", "unit", "amount"]
      }
    },
    "instructions": {
      "type": "array",
      "description": "Steps to prepare the recipe (no numbering)",
      "items": { "type": "string" }
    },
    "time_to_cook": {
      "type": "number",
      "description": "Total time to prepare the recipe in minutes"
    }
  },
  "required": ["ingredients", "instructions", "time_to_cook"]
}


openai.api_key = os.getenv("OPENAI_API_KEY")

def get_json(schema=default_schema, prompt=default_prompt, temperature=0):
    """_summary_

    Args:
        schema (dic, optional): the format of expected response. Defaults to default_schema.
        prompt (list, optional): list of prompts for GPT. Defaults to default_prompt.
        temperature (int, optional): how much gpt will generate confident content. Defaults to 0.

    Returns:
        _type_: response JSON in string
    """
    

    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=prompt,
    functions=[{"name": "own_function", "parameters": schema}],
    function_call={"name": "own_function"},
    temperature=temperature,
    )

    return completion.choices[0].message.function_call.arguments

