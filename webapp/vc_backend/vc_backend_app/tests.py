import os, subprocess, json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import VDImage, VCImage
from .enums import VDModel, VCModel

BASE_DIR = './webapp/vc_backend/'
STATIC_DIR = os.path.join(BASE_DIR, 'vc_backend_app/static/')

def check_image_name(response):
    image = response.data['image'].split('/')[-1] # camiones_qD4j27v.jpg
    image_extension = image.split('.')[-1] # jpg
    if len(image.split('_')) > 1:
        image_name = image.split('_')[0] # camiones
        check_image = image_name + '.' + image_extension # camiones.jpg
    else:
        check_image = image # camiones.jpg 
    return check_image

class VDImagePositiveTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        VDImage.objects.create(
            code = '1234567890AB',
            model = VDModel.YOLOV5S.value,
            image = SimpleUploadedFile(
                'camiones.jpg', 
                open(os.path.join(STATIC_DIR, 'detector/camiones.jpg'), 'rb').read(), 
                content_type='image/jpeg'
            ),
            inf_time = 0.534,
            label_count_dict = {'0;big truck': 2, '4;car': 5}
        )
        VDImage.objects.create(
            code = '0987654321BA',
            model = VDModel.YOLOV8S.value,
            image = SimpleUploadedFile(
                'coches.jpg', 
                open(os.path.join(STATIC_DIR, 'detector/coches.jpg'), 'rb').read(), 
                content_type='image/jpeg'
            ),
            inf_time = 0.732,
            label_count_dict = {'4;car': 20}
        )
    
    @classmethod
    def tearDownClass(cls):
        client = APIClient()
        client.delete('/detector/snapview/1234567890AB/')
        client.delete('/detector/snapview/0987654321BA/')
        super().tearDownClass()

    def test_list_vdimages_200(self):
        client = APIClient()
        response = client.get('/detector/snapzone/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_vdimage_yolov5s_201(self):
        client = APIClient()
        test_model = VDModel.YOLOV5S.value
        upload_image = open(os.path.join(STATIC_DIR, 'detector/carretera.jpg'), 'rb')
        test_image = SimpleUploadedFile(
            upload_image.name, 
            upload_image.read(), 
            content_type='image/jpeg'
        )
        test_vdimage_post_request = {
            'model': test_model,
            'image': test_image
        }
        response = client.post(
            '/detector/snapzone/', 
            test_vdimage_post_request, 
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VDImage.objects.count(), 3)
        # remove image from media after test
        image_path = os.path.join(BASE_DIR, response.data['image'].lstrip('/'))
        subprocess.run(['rm', image_path])

    def test_create_vdimage_yolov8s_201(self):
        client = APIClient()
        test_model = VDModel.YOLOV8S.value
        upload_image = open(os.path.join(STATIC_DIR, 'detector/vehiculos.webp'), 'rb')
        test_image = SimpleUploadedFile(
            upload_image.name, 
            upload_image.read(), 
            content_type='image/webp'
        )
        test_vdimage_post_request = {
            'model': test_model,
            'image': test_image
        }
        response = client.post(
            '/detector/snapzone/', 
            test_vdimage_post_request, 
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VDImage.objects.count(), 3)
        # remove image from media after test
        image_path = os.path.join(BASE_DIR, response.data['image'].lstrip('/'))
        subprocess.run(['rm', image_path])

    def test_retrieve_vdimage_200(self):
        client = APIClient()
        response = client.get('/detector/snapview/1234567890AB/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['model'], VDModel.YOLOV5S.value)
        self.assertEqual(check_image_name(response), 'camiones.jpg')
        self.assertEqual(response.data['inf_time'], 0.534)
        self.assertEqual(response.data['label_count_dict'], {'0;big truck': 2, '4;car': 5})

    def test_delete_vdimage_204(self):
        client = APIClient()
        response1 = client.delete('/detector/snapview/1234567890AB/')
        response2 = client.delete('/detector/snapview/0987654321BA/')
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response2.status_code, status.HTTP_204_NO_CONTENT)

class VDImageNegativeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        VDImage.objects.create(
            code = '1234567890AB',
            model = VDModel.YOLOV5S.value,
            image = SimpleUploadedFile(
                'camiones.jpg', 
                open(os.path.join(STATIC_DIR, 'detector/camiones.jpg'), 'rb').read(), 
                content_type='image/jpeg'
            ),
            inf_time = 0.534,
            label_count_dict = {'0;big truck': 2, '4;car': 5}
        )
        VDImage.objects.create(
            code = '0987654321BA',
            model = VDModel.YOLOV8S.value,
            image = SimpleUploadedFile(
                'coches.jpg', 
                open(os.path.join(STATIC_DIR, 'detector/coches.jpg'), 'rb').read(), 
                content_type='image/jpeg'
            ),
            inf_time = 0.732,
            label_count_dict = {'4;car': 20}
        )

    @classmethod
    def tearDownClass(cls):
        client = APIClient()
        client.delete('/detector/snapview/1234567890AB/')
        client.delete('/detector/snapview/0987654321BA/')
        super().tearDownClass()

    def test_create_vdimage_400(self):
        client = APIClient()
        upload_image = open(os.path.join(STATIC_DIR, 'detector/carretera.jpg'), 'rb')
        test_image = SimpleUploadedFile(
            upload_image.name, 
            upload_image.read(), 
            content_type='image/jpeg'
        )
        test_vdimage_post_request = {
            'model': '',
            'image': test_image
        }
        response = client.post(
            '/detector/snapzone/', 
            test_vdimage_post_request, 
            format='multipart'
        )
        error_message = json.loads(response.content.decode('utf-8'))['model'][0]
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error_message, 'This field is required.')
        self.assertEqual(VDImage.objects.count(), 2)

    def test_retrieve_vdimage_404(self):
        client = APIClient()
        response = client.get('/detector/snapview/000000000000/')
        error_message = json.loads(response.content.decode('utf-8'))['detail']
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(error_message, 'No VDImage matches the given query.')

    def test_delete_vdimage_404(self):
        client = APIClient()
        response = client.delete('/detector/snapview/000000000000/')
        error_message = json.loads(response.content.decode('utf-8'))['detail']
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(error_message, 'No VDImage matches the given query.')

class VCImagePositiveTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        VCImage.objects.create(
            code = '1234567890AC',
            model = VCModel.EFFNETB1.value,
            image = SimpleUploadedFile(
                'ferrari.jpg', 
                open(os.path.join(STATIC_DIR, 'classifier/ferrari.jpg'), 'rb').read(), 
                content_type='image/jpeg'
            ),
            inf_time = 1.032,
            pred_class = 'Ferrari FF Coupe 2012'
        )
        VCImage.objects.create(
            code = '0987654321CA',
            model = VCModel.YOLOV8SCLS.value,
            image = SimpleUploadedFile(
                'martin.jpg', 
                open(os.path.join(STATIC_DIR, 'classifier/martin.jpg'), 'rb').read(), 
                content_type='image/jpeg'
            ),
            inf_time = 0.958,
            pred_class = 'Aston Martin V8 Vantage Convertible 2012'
        )

    def test_list_vcimages_200(self):
        client = APIClient()
        response = client.get('/classifier/snapzone/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_vcimage_effnetb1_201(self):
        client = APIClient()
        test_model = VCModel.EFFNETB1.value
        upload_image = open(os.path.join(STATIC_DIR, 'classifier/mazda.jpg'), 'rb')
        test_image = SimpleUploadedFile(
            upload_image.name, 
            upload_image.read(), 
            content_type='image/jpeg'
        )
        test_vcimage_post_request = {
            'model': test_model,
            'image': test_image
        }
        response = client.post(
            '/classifier/snapzone/', 
            test_vcimage_post_request, 
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VCImage.objects.count(), 3)
        # remove image from media after test
        image_path = os.path.join(BASE_DIR, response.data['image'].lstrip('/'))
        subprocess.run(['rm', image_path])

    def test_create_vcimage_yolov8scls_201(self):
        client = APIClient()
        test_model = VCModel.YOLOV8SCLS.value
        upload_image = open(os.path.join(STATIC_DIR, 'classifier/ram.jpg'), 'rb')
        test_image = SimpleUploadedFile(
            upload_image.name, 
            upload_image.read(), 
            content_type='image/jpeg'
        )
        test_vcimage_post_request = {
            'model': test_model,
            'image': test_image
        }
        response = client.post(
            '/classifier/snapzone/', 
            test_vcimage_post_request, 
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VCImage.objects.count(), 3)
        # remove image from media after test
        image_path = os.path.join(BASE_DIR, response.data['image'].lstrip('/'))
        subprocess.run(['rm', image_path])

    def test_retrieve_vcimage_200(self):
        client = APIClient()
        response = client.get('/classifier/snapview/1234567890AC/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['model'], VCModel.EFFNETB1.value)
        self.assertEqual(check_image_name(response), 'ferrari.jpg')
        self.assertEqual(response.data['inf_time'], 1.032)
        self.assertEqual(response.data['pred_class'], 'Ferrari FF Coupe 2012')

    def test_delete_vcimage_204(self):
        client = APIClient()
        response1 = client.delete('/classifier/snapview/1234567890AC/')
        response2 = client.delete('/classifier/snapview/0987654321CA/')
        self.assertEqual(response1.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(response2.status_code, status.HTTP_204_NO_CONTENT)


class VCImageNegativeTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        VCImage.objects.create(
            code = '1234567890AC',
            model = VCModel.EFFNETB1.value,
            image = SimpleUploadedFile(
                'ferrari.jpg', 
                open(os.path.join(STATIC_DIR, 'classifier/ferrari.jpg'), 'rb').read(), 
                content_type='image/jpeg'
            ),
            inf_time = 1.032,
            pred_class = 'Ferrari FF Coupe 2012'
        )
        VCImage.objects.create(
            code = '0987654321CA',
            model = VCModel.YOLOV8SCLS.value,
            image = SimpleUploadedFile(
                'martin.jpg', 
                open(os.path.join(STATIC_DIR, 'classifier/martin.jpg'), 'rb').read(), 
                content_type='image/jpeg'
            ),
            inf_time = 0.958,
            pred_class = 'Aston Martin V8 Vantage Convertible 2012'
        )

    @classmethod
    def tearDownClass(cls):
        client = APIClient()
        client.delete('/classifier/snapview/1234567890AC/')
        client.delete('/classifier/snapview/0987654321CA/')
        super().tearDownClass()

    def test_create_vcimage_400(self):
        client = APIClient()
        upload_image = open(os.path.join(STATIC_DIR, 'classifier/mazda.jpg'), 'rb')
        test_image = SimpleUploadedFile(
            upload_image.name, 
            upload_image.read(), 
            content_type='image/jpeg'
        )
        test_vcimage_post_request = {
            'model': '',
            'image': test_image
        }
        response = client.post(
            '/classifier/snapzone/', 
            test_vcimage_post_request, 
            format='multipart'
        )
        error_message = json.loads(response.content.decode('utf-8'))['model'][0]
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error_message, 'This field is required.')
        self.assertEqual(VCImage.objects.count(), 2)

    def test_retrieve_vcimage_404(self):
        client = APIClient()
        response = client.get('/classifier/snapview/000000000000/')
        error_message = json.loads(response.content.decode('utf-8'))['detail']
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(error_message, 'No VCImage matches the given query.')

    def test_delete_vcimage_404(self):
        client = APIClient()
        response = client.delete('/classifier/snapview/000000000000/')
        error_message = json.loads(response.content.decode('utf-8'))['detail']
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(error_message, 'No VCImage matches the given query.')