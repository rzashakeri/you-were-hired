from django.contrib import admin
from users.models import UserType, User, SeekerProfile, SeekerSkill, Skill, EducationDetail, ExperienceDetail, Company


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """User Admin"""
    list_display = ["username", "first_name", "last_name", "gender", "user_type", "is_staff", "is_superuser"]
    list_filter = ["is_staff", "is_superuser", "user_type", "gender", "date_joined"]
    search_fields = ["first_name", "last_name", "username"]


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    """User Type Admin"""
    pass


@admin.register(SeekerProfile)
class SeekerProfileAdmin(admin.ModelAdmin):
    """Seeker Profile Admin"""
    list_display = ["__str__", "level", "birthday", "current_salary"]
    list_filter = ["level", "birthday", "current_salary"]


@admin.register(SeekerSkill)
class SeekerSkillAdmin(admin.ModelAdmin):
    """Seeker Skill Admin"""
    list_display = ["profile", "skill"]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    """Skill Admin"""
    pass


@admin.register(EducationDetail)
class EducationDetailAdmin(admin.ModelAdmin):
    """Education Detail Admin"""
    list_display = ["profile"]


@admin.register(ExperienceDetail)
class ExperienceDetailAdmin(admin.ModelAdmin):
    """Experience Detail Admin"""
    list_display = ["profile", "job_title", "company_name"]


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    """Experience Detail Admin"""
    list_display = ["user", "name", "company_website_url"]
