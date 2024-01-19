# Stay Gold, Cowboy

## Client-Side: React Next.JS
- [client side code](https://github.com/AngieMGonzalez/staygoldcowboy-client)

## Topics
- [Overview](#overview)
- [Get Started](#get-started)
- [MVP Features](#mvp-features)
- [Video Walkthrough of MVP](#video-walkthrough-of-mvp)
- [Relevant Links](#relevant-links)
- [Code Snippet](#code-snippet)
- [Project Screenshots](#mvp-project-screenshots)
- [Tech and Frameworks Used](#tech-and-frameworks-used)
- [Future Features](#future-features)
- [Contributors](#contributors)
___

## Overview
- The ideal user for Stay Gold, Cowboy is a fan of Sonatore
- Fans can sign in with Google authentication and upload their favorite image URLs of Sonatore's art
- Fans can organize the artwork by tags

## ERD
- [MVP ERD made with dbdiagrom.io](https://dbdiagram.io/d/64809033722eb77494910894)

## Wireframe
- [Wireframe created with Figma](https://www.figma.com/file/hOEfUiFeL3cMBTDBOCiQML/Stay-Gold%2C-Cowboy?type=design&node-id=0%3A1&t=ZmzcDnEjDJpCFnqX-1)

## Get Started
1. Clone Stay Gold, Cowboy to your local machine
```
git@github.com:AngieMGonzalez/staygoldcowboy-server.git
```
1. Move into the directory `cd staygoldcowboy-server`
2. *Optional run `pip install pyenv`
3. Install Python 3.9.16
4. Install pipenv `pip install pipenv`
5. Start your virtual environment `pipenv shell`
6. Run the Server by starting the debugger or running `python3 manage.py runserver`
7. Setup and run the [Stay Gold, Cowboy Client](https://github.com/AngieMGonzalez/staygoldcowboy-client) for this project to run on local machine.

## MVP Features
- Fans of Sonatore sign in with Firebase Google authentication
- Fans can browse all the art and all the tags
- Fans can create, read, update and delete art and tags
- Fans can create read update and delete their own snippet ideas
- Art has information regarding creation date, tags, and image url
- Fans can filter art by tags

## Video Walkthrough of MVP
- https://www.loom.com/share/c0f3bf90f50745d586bc2de0fa3b7ca2?sid=aca90b99-db81-4120-8330-390c45d06ba6

## Relevant Links
- [Figma Wireframes for MVP](https://www.figma.com/file/hOEfUiFeL3cMBTDBOCiQML/Stay-Gold%2C-Cowboy?type=design&node-id=0%3A1&t=ZmzcDnEjDJpCFnqX-1)
- [Project Board](https://github.com/users/AngieMGonzalez/projects/2)

## ERD

- [MVP ERD made with dbdiagrom.io](https://dbdiagram.io/d/64809033722eb77494910894)
<img width="500" alt="Stay Gold, Cowboy MVP ERD" src="https://user-images.githubusercontent.com/114124374/247436507-046a0270-51ee-4d4e-95a8-e74861da2cf6.png">

- Assumption: Art can have many tags, and tags can be associated with many pieces of art. 

## Code Snippet
Create an Art Obj
```
class ArtView(ViewSet):
    """SGC Art view viewsets"""

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized art instance
        """
        data = request.data
        fan = Fan.objects.get(uid=request.META['HTTP_AUTHORIZATION'])
        tag_ids = data["tagId"]

        new_art = Art.objects.create(
            fan=fan,
            title=data["title"],
            creation_date=data["creationDate"],
            image_url=data["imageUrl"],
        )

        for tag_id in tag_ids:
            tag = Tag.objects.get(pk=tag_id)
            new_art.tag.add(tag)

        serializer = ArtSerializer(new_art)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```


## MVP Project Screenshots
<img width="1000" alt="Stay Gold, Cowboy MVP Home Page" src="https://user-images.githubusercontent.com/114124374/250223135-c65c9156-002c-4cd6-b170-c4c9dcaf4565.png">

### Tech and Frameworks Used
<div align="center">  
    <a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50" /></a>  
    <a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/django-original.svg" alt="Django" height="50" /></a>
</div>
<div align="center"> 
    <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white" alt="SQLite" />
</div>

<div align="center">  
    <a href="https://firebase.google.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/firebase.png" alt="Firebase" height="50" /></a>  
</div>

### Future Features
- fans will be able to search through any description word or tag of on the art piece
- fans will be able to filter art by camera types used as well
- fans will be able to upload image files (JPG, IMG, PNG)

## Contributors
- [A.J. Gonzalez](https://github.com/gonzalez-aj)
- Badges from [Alexandre Sanlim](https://github.com/alexandresanlim/Badges4-README.md-Profile#see-more-repositories) and [Profilinator](https://profilinator.rishav.dev/)
- Client-Side React/Next.js Django Auth [template from Nashville Software School](https://github.com/codetracker-learning/TEMPLATE-nextjs-withauth-django)
- Thank you C62
