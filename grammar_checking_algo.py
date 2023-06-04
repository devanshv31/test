#grammar checking algorithm 
#code submitted by devansh verma 
from language_tool_python import LanguageTool

#tool = LanguageTool('en-US')
tool = language_tool_python.LanguageToolPublicAPI('en-US')


def grammar_check(text):
    # Perform grammar checking using LanguageTool
    matches = tool.check(text)
    
    # Print the grammar errors and their suggestions
    for match in matches:
        print("Error:", match.ruleId)
        print("Message:", match.message)
        print("Suggestions:", match.replacements)
        print("---")

# Example testcase 
input_text = "He don't have no time for that."


grammar_check(input_text)
