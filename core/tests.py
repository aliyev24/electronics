from django.test import TestCase
from django.urls import reverse
from .models import Feedback, Service, AboutUs, MainService, Statistics, ContactInformation



class FeedbackModelTest(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(
            name_surname='John Doe',
            text='This is a feedback text.',
            email='john@example.com',
            subject='Service Feedback'
        )

    def test_feedback_str(self):
        self.assertEqual(str(self.feedback), 'John Doe - Service Feedback')


class ServiceModelTest(TestCase):
    def setUp(self):
        self.service = Service.objects.create(
            title='Web Development',
            description='We offer web development services.'
        )

    def test_service_str(self):
        self.assertEqual(str(self.service), 'Web Development')


class AboutUsModelTest(TestCase):
    def setUp(self):
        self.about_us = AboutUs.objects.create(
            text='We are a company that values quality.'
        )

    def test_about_us_text(self):
        self.assertEqual(self.about_us.text, 'We are a company that values quality.')


class MainServiceModelTest(TestCase):
    def setUp(self):
        self.main_service = MainService.objects.create(
            service_name='Consulting',
            service_text='Expert consulting services available.'
        )

    def test_main_service_str(self):
        self.assertEqual(str(self.main_service), 'Consulting')


class StatisticsModelTest(TestCase):
    def setUp(self):
        self.statistics = Statistics.objects.create(
            experience_years=10,
            technician_number=5,
            satisfied_clients=100,
            complete_projects=50
        )

    def test_statistics_str(self):
        expected_str = 'Stats: 10 years, 5 techs, 100 clients, 50 projects'
        self.assertEqual(str(self.statistics), expected_str)


class ContactInformationModelTest(TestCase):
    def setUp(self):
        self.contact_info = ContactInformation.objects.create(
            address='123 Main St',
            email='contact@example.com',
            phone='123-456-7890'
        )

    def test_contact_info_str(self):
        expected_str = '123 Main St | contact@example.com | 123-456-7890'
        self.assertEqual(str(self.contact_info), expected_str)



class ViewsTestCase(TestCase):
    def setUp(self):
        self.service = Service.objects.create(title='Web Development', description='We offer web development services.')
        self.contact_info = ContactInformation.objects.create(address='123 Main St', email='contact@example.com', phone='123-456-7890')
        self.feedback = Feedback.objects.create(name_surname='John Doe', text='Great service!', email='john@example.com', subject='Feedback')
        self.statistic = Statistics.objects.create(experience_years=10, technician_number=5, satisfied_clients=100, complete_projects=50)
        self.main_service = MainService.objects.create(service_name='Consulting', service_text='Expert consulting services available.')

    def test_home_view(self):
        response = self.client.get(reverse('home'))  # Replace 'home' with the actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.service.title)
        self.assertContains(response, self.contact_info.address)
        self.assertContains(response, self.feedback.text)
        self.assertContains(response, str(self.statistic))
        self.assertContains(response, self.main_service.service_name)

    def test_about_view(self):
        response = self.client.get(reverse('about'))  # Replace 'about' with the actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, self.service.title)
        self.assertContains(response, self.contact_info.address)

    def test_services_view(self):
        response = self.client.get(reverse('services'))  # Replace 'services' with the actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'services.html')
        self.assertContains(response, self.service.title)

    def test_contact_view(self):
        response = self.client.get(reverse('contact'))  # Replace 'contact' with the actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertContains(response, self.contact_info.email)
