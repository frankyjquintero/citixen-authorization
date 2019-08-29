import uuid

from django.contrib.auth.models import Permission
from faker import Faker

from corexen.users.models import UserPermission, AppUser
from corexen.utils.testing import CitixenTestCase
from tests.test_companies.factories import CompanyFactory, HeadquarterFactory

fake = Faker()


class UserModelTestCase(CitixenTestCase):

    def setUp(self):
        self.user = self.make_user()
        self.app_user = AppUser.objects.create(uuid=self.user.uuid)
        self.company = CompanyFactory(created_by=self.app_user)
        self.headquarter = HeadquarterFactory(company=self.company, created_by=self.app_user)

    def test_should_add_permissions_to_user(self):
        self.assertEquals(self.app_user.user_permissions.count(), 0)
        perms_amount = Permission.objects.count()
        self.assertTrue(perms_amount > 0)
        perm_pks = Permission.objects.all().values_list('codename', flat=True)
        self._add_user_permissions(perms=perm_pks, user=self.app_user,
                                   headquarter=self.headquarter)
        self.assertEquals(perms_amount, self.app_user.user_permissions.count())

    def test_should_verify_if_user_has_a_given_permission(self):
        self.assertEquals(self.app_user.user_permissions.count(), 0)
        perm = Permission.objects.first()
        UserPermission.objects.create(user=self.app_user, permission=perm,
                                      headquarter=self.headquarter)
        self.assertEquals(self.app_user.user_permissions.count(), 1)
        perm_codename = '%s.%s.%s' % (perm.content_type.app_label, perm.codename,
                                      self.headquarter.pk)
        self.assertTrue(self.app_user.has_perm(perm_codename))

    def test_should_user_has_not_permission_in_another_headquarter_in_same_company(self):
        headquarter = HeadquarterFactory(company=self.company, created_by=self.app_user)
        self.assertEquals(self.app_user.user_permissions.count(), 0)
        perm_pks = Permission.objects.all().values_list('codename', flat=True)
        self._add_user_permissions(perms=perm_pks, user=self.app_user,
                                   headquarter=self.headquarter)
        perm = Permission.objects.first()
        perm_codename = '%s.%s.%s' % (perm.content_type.app_label, perm.codename,
                                      headquarter.pk)
        self.assertFalse(self.app_user.has_perm(perm_codename))

    def test_should_user_has_not_permission_in_another_headquarter_in_other_company(self):
        company = CompanyFactory(created_by=self.app_user)
        headquarter = HeadquarterFactory(company=company, created_by=self.app_user)
        self.assertEquals(self.app_user.user_permissions.count(), 0)
        perm_pks = Permission.objects.all().values_list('codename', flat=True)
        self._add_user_permissions(perms=perm_pks, user=self.app_user, headquarter=self.headquarter)
        perm = Permission.objects.first()
        perm_codename = '%s.%s.%s' % (perm.content_type.app_label, perm.codename, headquarter.pk)
        self.assertFalse(self.app_user.has_perm(perm_codename))


class AppUserModelTestCase(CitixenTestCase):

    def setUp(self):
        self.user = self.make_user()
        self.uuid = uuid.uuid1()
        self.appUser = AppUser.objects.create(uuid=self.uuid)

    def test_string_representation(self):
        self.assertEquals(str(self.appUser), 'Remote User: {}'.format(str(self.uuid)))
