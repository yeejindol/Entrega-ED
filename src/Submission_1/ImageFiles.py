# -*- coding: utf-8 -*-
"""
ImageFiles.py : ** REQUIRED ** El vostre codi de la classe ImageFiles.

Aquesta classe s'encarrega de gestionar el llistat d'arxius PNG dins la col·lecció d'imatges.

Funcionalitat:
    - Recórrer el filesystem a partir de ROOT_DIR per trobar tots els arxius PNG
    - Mantenir una representació en memòria dels arxius presents
    - Detectar quins arxius s'han afegit o eliminat des de l'última lectura
"""
import os
import cfg


class ImageFiles:

    def __init__(self):
        self._files = []
        self._added = []
        self._removed = []

    def __str__(self) -> str:
        return str(self._files)

    def reload_fs(self, path: str) -> None:
        # Recorre el directori especificat i actualitza la llista d'arxius PNG.
        # Detecta els arxius nous i els que s'han eliminat.
        current_files = []

        # Mateix recorregut que a cfg.get_one_file(), però només per a PNG.
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.lower().endswith(".png"):
                    full_path = os.path.join(root, filename)
                    relative_path = cfg.get_canonical_pathfile(full_path)
                    current_files.append(relative_path)

        self._added = []
        self._removed = []

        for file in current_files:
            if file not in self._files:
                self._added.append(file)

        for file in self._files:
            if file not in current_files:
                self._removed.append(file)

        self._files = current_files

    def files_added(self) -> list:
        # Retorna una llista (de strings) amb els paths relatius dels arxius
        # que s'han afegit des de l'última crida a reload_fs().
        result = []
        for file in self._added:
            result.append(file)
        return result
    
    def files_removed(self) -> list:
        # Retorna una llista (de strings) amb els paths relatius dels arxius
        # que s'han eliminat des de l'última crida a reload_fs().
        result = []
        for file in self._removed:
            result.append(file)
        return result

"""
Notes:
    - Els paths han de ser sempre relatius a ROOT_DIR
    - Només considereu arxius amb extensió .png (case-insensitive)
    - Heu de recórrer tots els subdirectoris recursivament
"""
