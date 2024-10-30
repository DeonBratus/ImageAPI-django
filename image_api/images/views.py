from rest_framework import viewsets
from .models import Image
from .serializers import ImageSerializer
from PIL import Image as PILImage 
from io import BytesIO
from django.core.files.base import ContentFile
from rest_framework.permissions import IsAuthenticated
from .tasks import image_event_log

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    
    #only for authentificated users
    permission_classes = [IsAuthenticated]
    
    TARGET_RESOLUTION = (100, 100)

    def perform_create(self, serializer):

        image_file = self.request.FILES['image_path']
        with PILImage.open(image_file) as img:

            # convert img to black-and-white filter
            img = img.convert('L')

            # buffer for imgs
            img_buffer = BytesIO() 

            # resize img with keeping form and save in memory
            img.thumbnail(self.TARGET_RESOLUTION)
            img.save(img_buffer, format="JPEG")
            img_buffer.seek(0)
            
            compressed_img = ContentFile(img_buffer.read(), name=f"compresed_{image_file.name}")

            resolution = f"{img.width}x{img.height}"
            size = compressed_img.size//1024 

            image = serializer.save(image_path=compressed_img,resolution=resolution, size=size) 

            image_event_log.delay("Uploaded", image.id)

