#importing module xml.etree.ElementTree  for ELementTree module from the xml package
import xml.etree.ElementTree as ET
#importing standard library  os
import os
#Flask frame work to build the web application
from flask import Flask, request, render_template

#Initialize FLask
app = Flask(__name__)


#This function will get the unique output file name
def get_filename(base_filename):

    #It saves the file name and extension in variables
    filename, ext = os.path.splitext(base_filename)
    counter=1

    #It checks the file name is already present or not if it is present it writes the new file name with number
    while os.path.exists(base_filename):

        #If the file with out_put_Value.txt is present it writes new file with out_put_value1.txt adds 1 at end of file name
        base_filename = f"{filename}{counter}{ext}"
        counter+=1

    #It will returns the new file name    
    return base_filename

#retrieve value and write it to a file
def retrieve_and_write(xml_file, target_id, output_file):

    #It checks for the xml file
    try:
        #It gets the full path of the xml file
        xml_file_path = os.path.join(os.path.dirname(__file__), xml_file)

        #parse the xml file using ElementTree module
        tree = ET.parse(xml_file_path)

        #root element for the xml file using ElementTree module
        root = tree.getroot()

        #Finds the element in the xml file with the target id
        element_target = root.find(".//*[@id='{}']".format(target_id))

        #if the element is found in the xml file
        if element_target is not None:

            #it will gets the target value from the xmlfile
            target_value = element_target.find("target").text

            #it will gets the output file name for the writing text file
            output_file = get_filename(output_file)

            #it will open the output file
            with open(output_file, "w") as f:

                #it will writes the target value in a output file
                f.write(target_value)

                #it will prints all values as for value, target_id and file name
                print(f"value '{target_value}' from element target with id '{target_id}' written to '{output_file}'.")

                #it will return all values for value, target_id and file name
                return target_value, output_file, target_value

        #if the id is not found in the xml file    
        else:
            print(f"No element with id '{target_id}' found in the xml file.")
            #it will return all values as non for value, target_id and file name
            return None, None, None
        
    #The error will generate if the xml file is not found
    except FileNotFoundError:

        #it will prints the messaage  file not found with specific xml file name
        print(f" Xml file '{xml_file}' not found.")

        #it will return all values as non for value, target_id and file name
        return None, None, None
    
    #different exceptions it will display here
    except Exception as e:

        #prints the what type of exception errror is occured
        print(f" Error type : {e}")

        #it will return all values as non for value, target_id and file name
        return None, None, None

#main page route with two methods GET and POST
@app.route('/', methods=['GET','POST'])
def main():

    if request.method=='POST':
        #sets xml file name 
        xml_file_name="sma_gentext.xml"
        #sets the target id
        target_id = request.form['target_id']
        #sets the out put file name with extension
        output_file_name = "out_put_value.txt"
        #it gets the actual value, filename, and id
        value, filename, id = retrieve_and_write(xml_file_name, target_id, output_file_name)

        #if the value is present in xml file 
        if value is not None:

            #It will display the page with value, filename, and id with the help of index.html
            return render_template('index.html', value=value, filename=filename, id=id)
        
        #if the value is not present in xml file
        else:
            
            #It will display the page with errorr message with the help of index.html
            return render_template('index.html', error_msg=f"No element with id '{target_id}' found in the xml file.")
    else:
        #It will return the index.html page if the method is GET 
        return render_template('index.html')

if __name__=='__main__':
    #The application will run on the port number 5000 in local host
    app.run(host='0.0.0.0',port=5000)