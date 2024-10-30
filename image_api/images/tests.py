from rest_framework.test import APITestCase, APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from images.models import Image
import os

from images.serializers import ImageSerializer
class ImageAPITest(APITestCase):

    def setUp(self):
        self.client = APIClient()
        # create test user
        self.user = User.objects.create_user(username='debral', password='12481632')

        # get token and authorization with them
        refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(refresh_token.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        
        # Creating file for testings
        self.img_path =\
        "/home/debral/devspace/abol-testing/image_api/media/images/compresed_Gigachad_Linux_penguin_in_comic_style_5WjvJqA.jpg"
        with open(self.img_path, 'rb') as img_file:
            self.img = SimpleUploadedFile(
                name="test_image.jpg",
                content=img_file.read(),
                content_type="image/jpeg"
            )

        self.image_instance = {
            "name": 'Test_IMG',
            # Here can be another data for Image
        }
    
        self.url = reverse('image-list')


    def test_create_and_edit_img(self):
        # creating test image
        response = self.client.post(self.url,
                                    {**self.image_instance, 'image_path': self.img}, 
                                    format="multipart")
        
        self.assertEqual(response.status_code, 201)
        

    def test_delete_img(self):
        # creating test image
        create_response = self.client.post(self.url,
                                        {**self.image_instance, 'image_path': self.img}, 
                                        format="multipart")
        self.assertEqual(create_response.status_code, 201)
        new_image_id = create_response.data['id']
        
        # deleting test img 
        delete_response = self.client.delete(reverse('image-detail', args=[new_image_id]))
        self.assertEqual(delete_response.status_code, 204)


    def tearDown(self):
        if os.path.exists(self.img.name):
            os.remove(self.img.name)
