import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextEdit, QDateTimeEdit 
import time
import os
import shutil
from PyQt5.QtWidgets import QFileDialog

class PostForm(QWidget):
  def __init__(self):
    super().__init__()

    self.initUI()

  def initUI(self):
    # Create input fields for each section of the JSON object
    writer_label = QLabel('Writer:', self)
    writer_label.move(50, 25)
    self.writer_field = QLineEdit(self)
    self.writer_field.move(100, 20)

    image_label = QLabel('Image:', self)
    image_label.move(50, 55)
    self.image_field = QLineEdit(self)
    self.image_field.move(100, 50)
    self.image_field.setReadOnly(True)

    image_button = QPushButton('Upload Image', self)
    image_button.move(250, 50)
    image_button.clicked.connect(self.uploadImage)

    caption_label = QLabel('Caption:', self)
    caption_label.move(50, 85)
    self.caption_field = QLineEdit(self)
    self.caption_field.move(100, 80)

    content_label = QLabel('Content:', self)
    content_label.move(50, 115)
    self.content_field = QTextEdit(self)
    self.content_field.move(100, 110)

    date_label = QLabel('Date:', self)
    date_label.move(50, 315)
    self.date_field = QDateTimeEdit(self)
    self.date_field.setDisplayFormat("yyyy-MM-dd'T'hh:mm:ss'Z'")
    self.date_field.move(100, 310)

    # Create a button to submit the form
    submit_button = QPushButton('Add', self)
    submit_button.move(25, 370)
    submit_button.clicked.connect(self.submitForm)

    # Create a button to update the site
    update_Button = QPushButton('Update', self)
    update_Button.move(125, 370)
    update_Button.clicked.connect(self.updateSite)

    # Create a button to quit the app
    exit_button = QPushButton("Exit", self)
    exit_button.move(315, 370)
    exit_button.clicked.connect(self.close)

    # Set the size and title of the window
    self.setGeometry(100, 100, 400, 400)
    self.setWindowTitle('Post Form')

  def uploadImage(self):
    # Open a file dialog to select an image file
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    file_name, _ = QFileDialog.getOpenFileName(self, 'Select Image', '', 'Image Files (*.png *.jpg *.jpeg *.gif)', options=options)

    # Copy the selected file to the "images/" folder
    if file_name:
      image_name = os.path.basename(file_name)
      shutil.copy(file_name, f'A:\Path\To\{image_name}')
      self.image_field.setText(image_name)

  def submitForm(self):
    # Read the current contents of the "posts.json" file
    with open('A:\Path\To\posts.json', 'r') as f:
      posts = json.load(f)

    # Create a new JSON object with the form data
    new_post = {
      'writer': self.writer_field.text(),
      'image': f'images/{self.image_field.text()}',
      'caption': self.caption_field.text(),
      'content': self.content_field.toPlainText(),
      'date': self.date_field.text()
    }

    # Add the new post to the beginning of the array
    posts.insert(0, new_post)

    # Write the updated JSON object back to the file
    with open('A:\Path\To\posts.json', 'w') as f:
      json.dump(posts, f, indent = 2)

    # Clear the input fields
    self.writer_field.setText('')
    self.image_field.setText('')
    self.caption_field.setText('')
    self.content_field.setText('')
    self.date_field.setText('')

  def updateSite(self):
    commit = "Post(s) Added"
    # Navigate to the directory where you want to initialize the Git repository
    os.chdir('A:\Path\To\KarandaGram')

    # Initialize the Git repository
    os.system('git init')

    # Add the remote origin
    os.system('git remote add origin https://github.com/Path/To/Repo')

    # Rename the branch to main
    os.system('git branch -M main')

    # Add all files to the staging area
    os.system('git add *')

    # Commit the changes
    os.system('git commit -m "' + commit + '"')

    # Push the changes to the remote repository
    os.system('git push -u origin main')

if __name__ == '__main__':
  app = QApplication(sys.argv)
  post_form = PostForm()
  post_form.show()
  sys.exit(app.exec_())
