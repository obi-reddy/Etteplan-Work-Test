import xml.etree.ElementTree as ET
import os
from flask import Flask, request, render_template

app = Flask(__name__)

def retrieve_and_write(xml_file, target_id, output_file):

    try:
        xml_file_path = os.path.join(os.path.dirname(__file__), xml_file)

        tree = ET.parse(xml_file_path)
        root = tree.getroot()

        element_target = root.find(".//*[@id='{}']".format(target_id))

        if element_target is not None:

            target_value = element_target.find("target").text

            with open(output_file, "w") as f:
                f.write(target_value)

                print(f"value '{target_value}' from element target with id '{target_id}' written to '{output_file}'.")

                return target_value, output_file, target_value
            
        else:
            return None, None, None
        
    except Exception as e:

        return None, None, None


@app.route('/', methods=['GET','POST'])
def main():

    if request.method=='POST':
        xml_file_name="sma_gentext.xml"

        target_id = request.form['target_id']

        output_file_name = "out_put_value.txt"

        value, filename, id = retrieve_and_write(xml_file_name, target_id, output_file_name)
    
        if value is not None:

            return render_template('index.html', value=value, filename=filename, id=id)
        
        else:

            return None

    return render_template('index.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)