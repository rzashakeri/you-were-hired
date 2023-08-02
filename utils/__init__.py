def logo_directory_path(instance, filename):
    file_name, file_extensions = filename.split('.')
    file_name = instance.slug
    path = "company/logo/images/"
    return "{0}/{1}.{2}".format(path, file_name, file_extensions)
