import os
from django.core.management.base import BaseCommand
from movie.models import Movie


class Command(BaseCommand):
    help = "Asigna imágenes a las películas desde la carpeta media/movie/images/images/"

    def handle(self, *args, **kwargs):
        images_dir = os.path.join('media', 'movie', 'images', 'images')
        updated_count = 0

        if not os.path.exists(images_dir):
            self.stderr.write(f"La carpeta de imágenes no existe: {images_dir}")
            return

        for movie in Movie.objects.all():
            filename = f"m_{movie.title}.png"
            image_path = os.path.join(images_dir, filename)

            if os.path.exists(image_path):
                # Cambia 'image' por el nombre real del campo de imagen en tu modelo si es diferente
                movie.image = os.path.join('movie', 'images', 'images', filename)
                movie.save()
                updated_count += 1
                self.stdout.write(self.style.SUCCESS(f"Imagen asignada: {movie.title}"))
            else:
                self.stderr.write(f"Imagen no encontrada para: {movie.title}")

        self.stdout.write(self.style.SUCCESS(f"Imágenes actualizadas para {updated_count} películas."))