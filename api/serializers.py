from rest_framework import serializers

from .models import Post, Comment, Follow, Group, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    def validate(self, data):
        # print(str(data.get('following')) + '  ' + str(self.user))
        if data.get('following') == self.context['request'].user:
            raise serializers.ValidationError(f'Follower shouldn\'t follow by oneself')
        return data

    class Meta:
        fields = '__all__'
        model = Follow


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'id')
        model = Group
