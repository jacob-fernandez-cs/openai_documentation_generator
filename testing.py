import openai 
import inspect
import re
import tkinter as tk

openai.api_key = "" #enter your current api key

#example python function for documentation
def sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr



def generate_docstring(my_func, python_version=3.7):
    # Grab the source code from the function as a string
    source_code = inspect.getsource(my_func)
    
    # Remove any existing docstring
    if my_func.__doc__ is not None:
        source_code = source_code.replace(my_func.__doc__,"")\
                                 .replace("\"\"\"","")

    # Wrap the source code with hints for GPT-3
    prompt = f"# Python {python_version}\n\n" \
           + source_code \
           + "\n# An elaborate, high quality docstring for the above function:\n\"\"\""

    # Send prompt to GPT-3
    response = openai.Completion.create(
                   model="text-davinci-003",
                   prompt=prompt,
                   temperature=0,
                   max_tokens=150,
                   top_p=1.0,
                   frequency_penalty=0.0,
                   presence_penalty=0.0,
                   stop=["#", "\"\"\""]
               )
    
    # Return the generated docstring
    docstring = response["choices"][0]["text"]
    return docstring


def generate_docstring2(source_code, python_version=3.7):
    # Remove any existing docstring
    source_code = source_code.replace("\"\"\"","") \
                             .replace("\'\'\'","")

    # Wrap the source code with hints for GPT-3
    prompt = f"# Python {python_version}\n\n" \
           + source_code \
           + "\n# An elaborate, high quality docstring for the above function:\n\"\"\""

    # Send prompt to GPT-3
    response = openai.Completion.create(
                   model="text-davinci-003",
                   prompt=prompt,
                   temperature=0,
                   max_tokens=150,
                   top_p=1.0,
                   frequency_penalty=0.0,
                   presence_penalty=0.0,
                   stop=["#", "\"\"\""]
               )

    # Return the generated docstring
    docstring = response["choices"][0]["text"]
    return docstring


def generate_java_doc(java_function):
    # Strip out any comments in the Java function
    java_function = re.sub(r'//.*?\n|/\*.*?\*/', '', java_function, flags=re.S)
    
    # Construct the prompt for the API request
    prompt = f"Generate an elaborate documentation for the following Java function:\n\n{java_function}"
    
    # Call the OpenAI GPT-3 API to generate documentation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=512,
        n=1,
        stop=None,
        timeout=10
    )
    
    # Extract the generated documentation from the API response
    generated_doc = response.choices[0].text.strip()
    
    # Return the generated documentation as a string
    return generated_doc

def generate_js_doc(js_function):
    # Strip out any comments in the JavaScript function
    js_function = re.sub(r'//.*?\n|/\*.*?\*/', '', js_function, flags=re.S)

    # Construct the prompt for the API request
    prompt = f"Generate an elaborate documentation for the following JavaScript function:\n\n{js_function}"

    # Call the OpenAI GPT-3 API to generate documentation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=512,
        n=1,
        stop=None,
        timeout=10
    )

    # Extract the generated documentation from the API response
    generated_doc = response.choices[0].text.strip()

    # Return the generated documentation as a string
    return generated_doc


def generate_cpp_doc(cpp_function):
    # Strip out any comments in the C++ function
    cpp_function = re.sub(r'//.*?\n|/\*.*?\*/', '', cpp_function, flags=re.S)

    # Construct the prompt for the API request
    prompt = f"Generate an elaborate documentation for the following C++ function:\n\n{cpp_function}"

    # Call the OpenAI GPT-3 API to generate documentation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=512,
        n=1,
        stop=None,
        timeout=10
    )

    # Extract the generated documentation from the API response
    generated_doc = response.choices[0].text.strip()

    # Return the generated documentation as a string
    return generated_doc

def generate_csharp_doc(csharp_function):
    # Strip out any comments in the C# function
    csharp_function = re.sub(r'//.*?\n|/\*.*?\*/', '', csharp_function, flags=re.S)

    # Construct the prompt for the API request
    prompt = f"Generate an elaborate documentation for the following C# function:\n\n{csharp_function}"

    # Call the OpenAI GPT-3 API to generate documentation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=512,
        n=1,
        stop=None,
        timeout=10
    )

    # Extract the generated documentation from the API response
    generated_doc = response.choices[0].text.strip()

    # Return the generated documentation as a string
    return generated_doc

def generate_ruby_doc(ruby_function):
    # Strip out any comments in the Ruby function
    ruby_function = re.sub(r'#.*?\n|=\begin\n.*?\n=end', '', ruby_function, flags=re.S)

    # Construct the prompt for the API request
    prompt = f"Generate an elaborate documentation for the following Ruby function:\n\n{ruby_function}"

    # Call the OpenAI GPT-3 API to generate documentation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=512,
        n=1,
        stop=None,
        timeout=10
    )

    # Extract the generated documentation from the API response
    generated_doc = response.choices[0].text.strip()

    # Return the generated documentation as a string
    return generated_doc

def generate_php_doc(php_function):
    # Strip out any comments in the PHP function
    php_function = re.sub(r'\/\/.*?\n|\/\*.*?\*\/', '', php_function, flags=re.S)

    # Construct the prompt for the API request
    prompt = f"Generate an elaborate documentation for the following PHP function:\n\n{php_function}"

    # Call the OpenAI GPT-3 API to generate documentation
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=512,
        n=1,
        stop=None,
        timeout=10
    )

    # Extract the generated documentation from the API response
    generated_doc = response.choices[0].text.strip()

    # Return the generated documentation as a string
    return generated_doc


#example functions as strings

java_function = """
public static void bubbleSort(int[] arr) {
    int n = arr.length;
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // swap arr[j] and arr[j+1]
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}
"""
javaScript_function = """ 
function sortAndFindLongest(arr) {
  const sortedArr = arr.sort(function(a, b) {
    return a.localeCompare(b);
  });
  const longestString = sortedArr.reduce(function(a, b) {
    return a.length > b.length ? a : b;
  });
  return [sortedArr, longestString];
}
"""

cpp_function = """int findLargest(int arr[], int size) {
    int largest = arr[0];
    for (int i = 1; i < size; i++) {
        if (arr[i] > largest) {
            largest = arr[i];
        }
    }
    return largest;
} """
csharp_function = """public int[] FilterEvenNumbers(int[] numbers)
{
    List<int> evenNumbersList = new List<int>();

    for (int i = 0; i < numbers.Length; i++)
    {
        if (numbers[i] % 2 == 0)
        {
            evenNumbersList.Add(numbers[i]);
        }
    }

    return evenNumbersList.ToArray();
}
"""

ruby_function = """def scrape_website(url)
  # Use Nokogiri to parse the HTML from the website
  doc = Nokogiri::HTML(open(url))

  # Extract information from the HTML using Nokogiri methods
  title = doc.css('title').text.strip
  links = doc.css('a').map { |link| link['href'] }.compact

  # Return the extracted information
  return { title: title, links: links }
end"""

php_function = """ function generatePassword($length = 10) {
    $chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    $password = '';
    for ($i = 0; $i < $length; $i++) {
        $password .= $chars[rand(0, strlen($chars) - 1)];
    }
    return $password;
}
"""


#all of the examples showing off the documentation generation are commented out, openapi does not like multiple different requests being made at the same time uncomment the examples
#one at a time for testing

#generated_php_doc = generate_php_doc(php_function)
#print(generated_php_doc)


#my_docstring= generate_docstring(sort)
#print(my_docstring)

#generated_ruby_doc = generate_ruby_doc(ruby_function)
#print(generated_ruby_doc)

#generated_cpp_doc = generate_cpp_doc(cpp_function)
#print(generated_cpp_doc)

#generated_csharp_doc = generate_csharp_doc(csharp_function)
#print(generated_csharp_doc)

#generated_javaScript_doc = generate_js_doc(javaScript_function)
#print(generated_javaScript_doc)


generated_doc_java = generate_java_doc(java_function)
print(generated_doc_java)






def store_input():
    global input_str
    input_str = input_box.get()
    output_label.config(text=input_str)  # update the text of the output label

def python_gui():
    global input_str
    input_str = input_box.get()
    processed_str = generate_docstring2(input_str)  # process the input string
    output_label.config(text=processed_str)



def java_gui():
    global input_str
    input_str = input_box.get()
    processed_str = generate_java_doc(input_str)  # process the input string
    output_label.config(text=processed_str)


def javaScript_gui():
    global input_str
    input_str = input_box.get()
    processed_str = generate_js_doc(input_str)  # process the input string
    output_label.config(text=processed_str)


def cpp_gui():
    global input_str
    input_str = input_box.get()
    processed_str = generate_cpp_doc(input_str)  # process the input string
    output_label.config(text=processed_str)


def csharp_gui():
    global input_str
    input_str = input_box.get()
    processed_str = generate_csharp_doc(input_str)  # process the input string
    output_label.config(text=processed_str)

def php_gui():
    global input_str
    input_str = input_box.get()
    processed_str = generate_php_doc(input_str)  # process the input string
    output_label.config(text=processed_str)

def ruby_gui():
    global input_str
    input_str = input_box.get()
    processed_str = generate_ruby_doc(input_str)  # process the input string
    output_label.config(text=processed_str)






# create the GUI window
root = tk.Tk()
root.geometry("720x720")  # set the size of the window

# create the text input box
input_box = tk.Entry(root, width=50)
input_box.pack()

# create the submit buttons
submit_button1 = tk.Button(root, text="python", command=python_gui)
submit_button1.pack(side=tk.TOP, pady=5)
submit_button2 = tk.Button(root, text="java", command=java_gui)
submit_button2.pack(side=tk.TOP, pady=5)
submit_button3 = tk.Button(root, text="c++", command=cpp_gui)
submit_button3.pack(side=tk.TOP, pady=5)
submit_button4 = tk.Button(root, text="c#", command=csharp_gui)
submit_button4.pack(side=tk.TOP, pady=5)
submit_button5 = tk.Button(root, text="ruby", command=ruby_gui)
submit_button5.pack(side=tk.TOP, pady=5)
submit_button6 = tk.Button(root, text="php", command=php_gui)
submit_button6.pack(side=tk.TOP, pady=5)

# create the label for output
output_label = tk.Label(root, text="")
output_label.pack()

# start the main event loop
root.mainloop()





