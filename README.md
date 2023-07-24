# Etteplan-Work-Test
<h2>Introduction</h2>
This web application is created using the Flask framework, designed to fetch a specific value from an XML file (sma_gentext.xml) using a provided target ID. To ensure that existing files are not overwritten, the retrieved value is saved to a text file (out_put_value.txt) with a unique name.

<h2>Prerequisites</h2>
<p>Python 3.8.0</p>

<p>Flask library installed. install it using: "pip install Flask"</p>

<h2>How to use the application</h2>
<h3>1. Clone the repository to your local machine using the command:</h3>
<h4>     git clone https://github.com/obi-reddy/Etteplan-Work-Test.git</h4>
<h3>2. Navigate to the cloned repository directory.</h3>
<h3>3. Run the Flask application by executing the following command in the terminal:</h3>
<h4>      python app.py</h4>
<h3>4. Access the application in your web browser at http://localhost:5000/</h3>
<h3>5. Enter a valid target ID (e.g., 42007) in the input field and click "Submit."</h3>
<h3>6. The application will retrieve the value from the XML file (sma_gentext.xml) for the specified target ID and save it to a unique output file (out_put_value.txt).</h3>
<h3>7. The Results successfully saved in a project folder it will be displayed on the webpage.</h3>
<h3>8. If the target ID is not found in the XML file or an error occurs, an error message will be shown.</h3>
<h3>9. If successful, you can download the output file containing the retrieved value using the "Download Result"</h3>
<h3>10. You can repeat the process by entering different target IDs and clicking "Submit" again.</h3>

