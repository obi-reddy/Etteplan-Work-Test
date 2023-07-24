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


<h1> simple way to Use the application using Docker</h1>
<h1>To run the Docker image you need to follow these steps:</h1>
<h2>Step 1: Open your web browser and go to the Docker website: https://www.docker.com/ Create account and install the docker</h2>
<h2>Step 2: After installing Docker on your system login to Docker</h2>
<h2>Step 3: Open terminal and Pull the Docker Image: Use the "docker pull" command to download the Docker image from the Docker Hub repository:</h2>
<h4>docker pull obireddy572/work_test_app:latest</h4>
<h2>Step 4: Run the Docker Container: After pulling the image, you can use the "docker run" command to start the container:</h2>
<h4>docker run -d -p 5000:5000 obireddy572/work_test_app:latest </h4>
Explanation of the command:   
                           -d: Detach the container and run it in the background.
                           -p 5000:5000: Map port 5000 of the host to port 5000 inside the container.
                           obireddy572/work_test_app:latest: This specifies the name and version (tag) of the Docker image to run.
                           With this command, you can access the application in your web browser by navigating to http://localhost:5000
                           


<h1>Resutls of screenshots with web Application </h1>
<h2>Screen shot 1</h2>
![Screenshot 1](https://github.com/obi-reddy/Etteplan-Work-Test/raw/cbab4e71a9288d8c0c21a6edc6d2de3ed61465ea/screenshots/screenshot1.png)
<h2>Screen shot 2: Target element id 42007</h2>
![image](https://github.com/obi-reddy/Etteplan-Work-Test/assets/93593081/5925e3ba-49b8-45de-b92b-ddb367fee601)
<h2>Screen shot 3: With target element id 4200</h2>
![image](https://github.com/obi-reddy/Etteplan-Work-Test/assets/93593081/3621bc48-15c1-4348-b41c-0ecb22ba0f30)
<h2>Screen shot 4: With entering Alphabets</h2>
![image](https://github.com/obi-reddy/Etteplan-Work-Test/assets/93593081/6b55b87e-4b5c-4506-bc68-56ce80d0fa3a)
<h2>Screen shot 5: with empty target id</h2>
![image](https://github.com/obi-reddy/Etteplan-Work-Test/assets/93593081/ed02cf9f-0983-4384-8fd2-06aa8b605b3f)






