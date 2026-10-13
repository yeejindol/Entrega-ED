# -*- coding: utf-8 -*-
"""
Gallery.py : ** REQUIRED ** El vostre codi de la classe Gallery.

Aquesta classe s'encarrega de gestionar galeries d'imatges en format JSON.

Funcionalitat:
    - Llegir galeries des d'arxius JSON
    - Visualitzar totes les imatges d'una galeria
    - Afegir i eliminar imatges de la galeria

Format JSON d'una galeria:
{
  "gallery_name": "Cyberpunk Cities",
  "description": "Collection of futuristic urban landscapes",
  "created_date": "2025-09-30",
  "images": [
    "generated_images/city_001.png",
    "generated_images/city_neon_12.png",
    "generated_images/urban_street_45.png"
  ]
}

Mètodes a implementar:
    - load_file(file: str) -> None
        Llegeix un arxiu JSON amb la definició de la galeria.
        Ha de validar que cada imatge referenciada existeix a la col·lecció.
        Si una imatge no existeix, l'ignora i continua processant.
        Emmagatzema internament els UUID de les imatges vàlides.

    - show() -> None
        Visualitza totes les imatges de la galeria en ordre utilitzant
        ImageViewer.show_image().

    - add_image_at_end(uuid: str) -> None
        Afegeix una imatge al final de la galeria.

    - remove_first_image() -> None
        Elimina la primera imatge de la galeria.

    - remove_last_image() -> None
        Elimina l'última imatge de la galeria.

Notes:
    - Utilitzeu la llibreria json per llegir els arxius
    - Els paths dins el JSON són relatius a ROOT_DIR
    - Cada galeria és un objecte independent (instància de Gallery)
    - Podeu tenir múltiples galeries actives simultàniament
    - Les operacions d'afegir/eliminar són ràpides (no busquen a la llista)
"""

import json
import os
import cfg


class Gallery:
    def __init__(self, image_id=None, image_viewer=None):
        self._image_id = image_id
        self._image_viewer = image_viewer
        self.gallery_name = ""
        self.description = ""
        self.created_date = ""
        self.images = []

    def load_file(self, file: str) -> None:
        # image_id ha de ser el registre de la col·lecció.
        if self._image_id is None:
            raise ValueError("Gallery necessita un ImageID per carregar imatges.")

        with open(file, "r", encoding="utf-8") as gallery_file:
            data = json.load(gallery_file)

        self.gallery_name = data.get("gallery_name", "")
        self.description = data.get("description", "")
        self.created_date = data.get("created_date", "")
        self.images = []

        for relative_path in data["images"]:
            full_path = os.path.join(cfg.ROOT_DIR, relative_path)
            if os.path.isfile(full_path):
                canonical_path = cfg.get_canonical_pathfile(full_path)
                image_uuid = self._image_id.get_uuid(canonical_path)
                if image_uuid is not None:
                    self.images.append(image_uuid)

    def show(self) -> None:
        if self.images and self._image_viewer is None:
            raise ValueError("Gallery necessita un ImageViewer per mostrar imatges.")

        for image_uuid in self.images:
            self._image_viewer.show_image(image_uuid, cfg.DISPLAY_MODE)
