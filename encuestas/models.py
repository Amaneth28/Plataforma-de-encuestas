import uuid

from django.conf import settings
from django.db import models


# =========================================================
# PERFIL DE USUARIO
# =========================================================

class PerfilUsuario(models.Model):

    class Rol(models.TextChoices):
        ADMINISTRADOR = "administrador", "Administrador"
        CREADOR = "creador", "Creador"
        PARTICIPANTE = "participante", "Participante"

    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="perfil"
    )

    rol = models.CharField(
        max_length=20,
        choices=Rol.choices,
        default=Rol.PARTICIPANTE
    )

    telefono = models.CharField(
        max_length=20,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.get_rol_display()}"


# =========================================================
# CATEGORÍA
# =========================================================

class Categoria(models.Model):

    nombre = models.CharField(
        max_length=100,
        unique=True
    )

    descripcion = models.TextField(
        blank=True
    )

    activa = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre


# =========================================================
# ENCUESTA
# =========================================================

class Encuesta(models.Model):

    class Estado(models.TextChoices):
        BORRADOR = "borrador", "Borrador"
        PUBLICADA = "publicada", "Publicada"
        CERRADA = "cerrada", "Cerrada"

    class Privacidad(models.TextChoices):
        PUBLICA = "publica", "Pública"
        PRIVADA = "privada", "Privada"

    creador = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="encuestas_creadas"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="encuestas"
    )

    titulo = models.CharField(
        max_length=150
    )

    descripcion = models.TextField()

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.BORRADOR
    )

    privacidad = models.CharField(
        max_length=20,
        choices=Privacidad.choices,
        default=Privacidad.PUBLICA
    )

    anonima = models.BooleanField(
        default=False
    )

    fecha_inicio = models.DateTimeField(
        null=True,
        blank=True
    )

    fecha_cierre = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo


# =========================================================
# PREGUNTA
# =========================================================

class Pregunta(models.Model):

    class Tipo(models.TextChoices):
        TEXTO_CORTO = "texto_corto", "Texto corto"
        TEXTO_LARGO = "texto_largo", "Texto largo"
        OPCION_UNICA = "opcion_unica", "Opción única"
        OPCION_MULTIPLE = "opcion_multiple", "Opción múltiple"
        SI_NO = "si_no", "Sí / No"
        ESCALA = "escala", "Escala"

    encuesta = models.ForeignKey(
        Encuesta,
        on_delete=models.CASCADE,
        related_name="preguntas"
    )

    texto = models.CharField(
        max_length=255
    )

    tipo = models.CharField(
        max_length=30,
        choices=Tipo.choices
    )

    obligatoria = models.BooleanField(
        default=True
    )

    orden = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.texto


# =========================================================
# OPCIÓN
# =========================================================

class Opcion(models.Model):

    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        related_name="opciones"
    )

    texto = models.CharField(
        max_length=150
    )

    valor = models.IntegerField(
        null=True,
        blank=True
    )

    orden = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["orden"]

    def __str__(self):
        return self.texto


# =========================================================
# PARTICIPACIÓN
# =========================================================

class Participacion(models.Model):

    class Estado(models.TextChoices):
        INICIADA = "iniciada", "Iniciada"
        COMPLETADA = "completada", "Completada"
        ABANDONADA = "abandonada", "Abandonada"

    encuesta = models.ForeignKey(
        Encuesta,
        on_delete=models.CASCADE,
        related_name="participaciones"
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="participaciones"
    )

    fecha_inicio = models.DateTimeField(
        auto_now_add=True
    )

    fecha_fin = models.DateTimeField(
        null=True,
        blank=True
    )

    completada = models.BooleanField(
        default=False
    )

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.INICIADA
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.encuesta.titulo} - {self.estado}"


# =========================================================
# RESPUESTA
# =========================================================

class Respuesta(models.Model):

    participacion = models.ForeignKey(
        Participacion,
        on_delete=models.CASCADE,
        related_name="respuestas"
    )

    pregunta = models.ForeignKey(
        Pregunta,
        on_delete=models.CASCADE,
        related_name="respuestas"
    )

    respuesta_texto = models.TextField(
        blank=True
    )

    respuesta_numero = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    respuesta_booleano = models.BooleanField(
        null=True,
        blank=True
    )

    fecha_respuesta = models.DateTimeField(
        auto_now_add=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["participacion", "pregunta"],
                name="respuesta_unica_por_pregunta"
            )
        ]

    def __str__(self):
        return f"Respuesta - {self.pregunta.texto}"


# =========================================================
# OPCIONES SELECCIONADAS EN UNA RESPUESTA
# =========================================================

class RespuestaOpcion(models.Model):

    respuesta = models.ForeignKey(
        Respuesta,
        on_delete=models.CASCADE,
        related_name="opciones_seleccionadas"
    )

    opcion = models.ForeignKey(
        Opcion,
        on_delete=models.CASCADE,
        related_name="respuestas_seleccionadas"
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["respuesta", "opcion"],
                name="opcion_unica_por_respuesta"
            )
        ]

    def __str__(self):
        return f"{self.respuesta} - {self.opcion}"


# =========================================================
# INVITACIÓN
# =========================================================

class Invitacion(models.Model):

    class Estado(models.TextChoices):
        PENDIENTE = "pendiente", "Pendiente"
        ACEPTADA = "aceptada", "Aceptada"
        RECHAZADA = "rechazada", "Rechazada"
        VENCIDA = "vencida", "Vencida"

    encuesta = models.ForeignKey(
        Encuesta,
        on_delete=models.CASCADE,
        related_name="invitaciones"
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="invitaciones"
    )

    token = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.PENDIENTE
    )

    fecha_envio = models.DateTimeField(
        auto_now_add=True
    )

    fecha_uso = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["encuesta", "usuario"],
                name="invitacion_unica_por_usuario"
            )
        ]

    def __str__(self):
        return f"{self.usuario.username} - {self.encuesta.titulo}"


# =========================================================
# AUDITORÍA
# =========================================================

class Auditoria(models.Model):

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="acciones_auditoria"
    )

    encuesta = models.ForeignKey(
        Encuesta,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="auditorias"
    )

    accion = models.CharField(
        max_length=50
    )

    descripcion = models.TextField(
        blank=True
    )

    ip_origen = models.GenericIPAddressField(
        null=True,
        blank=True
    )

    fecha_evento = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.accion