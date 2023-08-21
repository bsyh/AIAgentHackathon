from gpt_utils import get_json


prompt = [
    {"role": "system", "content": "You are a helpful assistant. You give advices for university master programs."},
    {"role": "user", "content": "Provide a list of schools in Canada that has strong computer science program."}
  ]

schema = {
  

  "type": "object",
  "properties": {
    "school_list": {
      "type": "array",
      "description": "school name available for program application",
      "items": { "type": "string" }
    },
  },
  "required": ["school_list"]
}

print(get_json(prompt=prompt, schema=schema))

"""
Result will be returned in JSON such as:


{
  "school_list": [
    "University of Toronto",
    "University of British Columbia",
    "McGill University",
    "University of Waterloo",
    "University of Alberta",
    "University of Montreal",
    "Simon Fraser University",
    "University of Ottawa",
    "University of Calgary",
    "University of Victoria"
  ]
}
"""