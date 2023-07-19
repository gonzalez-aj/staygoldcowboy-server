import json
from rest_framework import status
from rest_framework.test import APITestCase
from staygoldcowboyapi.models import Art, Fan, Tag
from rest_framework.authtoken.models import Token


class ArtTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['art', 'fans', 'tags', 'users']

    # If you need to have any resources created before a test is run
    # you can do that in setUp()
    def setUp(self):
        # 1. Registers a user in the testing database.
        self.fan = Fan.objects.first()
        token = Token.objects.get(user=self.fan.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
        # 2. Seeds the testing database with a game type

    def test_create_game(self):
        """
        Ensure we can create a new game. POST
        """
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/arts"

        # Define the request body
        # this is supposed to be client
        data = {
            "fanId": 1,
            "title": "Clue",
            "imageUrl": "www.google.com",
            "createdOn": "2020-01-01",
            "tag": [1, 2]
        }

        # Initiate request and store response
        # fake test
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["title"], "Clue")
        self.assertEqual(json_response["imageUrl"], "www.google.com")
        self.assertEqual(json_response["created_on"], "2020-01-01")
        self.assertEqual(json_response["tag"], [1, 2])

    # def test_get_game(self):
    #     """
    #     Ensure we can get an existing game.
    #     """

    #     # Seed the database with a game
    #     game = Game()
    #     game.game_type_id = 1
    #     game.skill_level = 5
    #     game.title = "Monopoly"
    #     game.maker = "Milton Bradley"
    #     game.number_of_players = 4
    #     game.gamer_id = 1

    #     game.save()

    #     # Initiate request and store response
    #     response = self.client.get(f"/games/{game.id}")

    #     # Parse the JSON in the response body
    #     json_response = json.loads(response.content)

    #     # Assert that the game was retrieved
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Assert that the values are correct
    #     self.assertEqual(json_response["title"], "Monopoly")
    #     self.assertEqual(json_response["maker"], "Milton Bradley")
    #     self.assertEqual(json_response["skill_level"], 5)
    #     self.assertEqual(json_response["number_of_players"], 4)

    # def test_change_game(self):
    #     """
    #     Ensure we can change an existing game.
    #     Testing PUT
    #     """
    #     game = Game()
    #     game.game_type_id = 1
    #     game.skill_level = 5
    #     game.title = "Sorry"
    #     game.maker = "Milton Bradley"
    #     game.number_of_players = 4
    #     game.gamer_id = 1
    #     game.save()

    #     # DEFINE NEW PROPERTIES FOR GAME
    #     data = {
    #         "gameTypeId": 1,
    #         "skillLevel": 2,
    #         "title": "Sorry",
    #         "maker": "Hasbro",
    #         "numberOfPlayers": 4
    #     }

    #     response = self.client.put(f"/games/{game.id}", data, format="json")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     # GET game again to verify changes were made
    #     response = self.client.get(f"/games/{game.id}")
    #     json_response = json.loads(response.content)

    #     # Assert that the properties are correct
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(json_response["title"], "Sorry")
    #     self.assertEqual(json_response["maker"], "Hasbro")
    #     self.assertEqual(json_response["skill_level"], 2)
    #     self.assertEqual(json_response["number_of_players"], 4)

    # def test_delete_game(self):
    #     """
    #     Ensure we can delete an existing game.
    #     """
    #     game = Game()
    #     game.game_type_id = 1
    #     game.skill_level = 5
    #     game.title = "Sorry"
    #     game.maker = "Milton Bradley"
    #     game.number_of_players = 4
    #     game.gamer_id = 1
    #     game.save()

    #     # DELETE the game you just created
    #     response = self.client.delete(f"/games/{game.id}")
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     # GET the game again to verify you get a 404 response - this is the retrieve
    #     response = self.client.get(f"/games/{game.id}")
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
