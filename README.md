# Stay Gold, Cowboy

## Client-Side: React Next.JS
- [client side code](https://github.com/AngieMGonzalez/staygoldcowboy-client)

## Topics
- [Overview](#overview)
- [MVP Features](#mvp-features)
- [Relevant Links](#relevant-links)
- [Code Snippet](#code-snippet)
- [Project Screenshots](#project-screenshots)
- [Get Started](#get-started)
- [Tech and Frameworks Used](#tech-and-frameworks-used)
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


## Project Screenshots

### Tech and Frameworks Used
<div align="center">  
<a href="https://www.python.org/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50" /></a>  
<a href="https://www.djangoproject.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/django-original.svg" alt="Django" height="50" /></a>  
</div>


### Google Auth
<div align="center">  
<a href="https://firebase.google.com/" target="_blank"><img style="margin: 10px" src="https://profilinator.rishav.dev/skills-assets/firebase.png" alt="Firebase" height="50" /></a>  
</div>

## Contributors
- [Angie Gonzalez](https://github.com/AngieMGonzalez)
- Badges from [Alexandre Sanlim](https://github.com/alexandresanlim/Badges4-README.md-Profile#see-more-repositories)
- React/Next.js Django Auth [template from Nashville Software School](https://github.com/codetracker-learning/TEMPLATE-nextjs-withauth-django)
