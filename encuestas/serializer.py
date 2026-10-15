from rest_framework import serializers

from .models import (
    PerfilUsuario,
    Categoria,
    Encuesta,
    Pregunta,
    Opcion,
    Participacion,
    Respuesta,
    RespuestaOpcion,
    Invitacion,
    Auditoria,
)


class PerfilUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilUsuario
        fields = ('id', 'usuario', 'rol', 'telefono')


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id', 'nombre', 'descripcion', 'activa')


class EncuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Encuesta
        fields = (
            'id', 'creador', 'categoria', 'titulo',
            'descripcion', 'estado', 'privacidad',
            'anonima', 'fecha_inicio', 'fecha_cierre'
        )


class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = (
            'id', 'encuesta', 'texto', 'tipo',
            'obligatoria', 'orden'
        )


class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ('id', 'pregunta', 'texto', 'valor', 'orden')


class ParticipacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participacion
        fields = (
            'id', 'encuesta', 'usuario',
            'fecha_inicio', 'fecha_fin',
            'completada', 'estado'
        )


class RespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Respuesta
        fields = (
            'id', 'participacion', 'pregunta',
            'respuesta_texto', 'respuesta_numero',
            'respuesta_booleano', 'fecha_respuesta'
        )


class RespuestaOpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestaOpcion
        fields = ('id', 'respuesta', 'opcion')


class InvitacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invitacion
        fields = (
            'id', 'encuesta', 'usuario',
            'estado', 'fecha_envio', 'fecha_uso'
        )


class AuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditoria
        fields = (
            'id', 'usuario', 'encuesta',
            'accion', 'descripcion',
            'ip_origen', 'fecha_evento'
        )
