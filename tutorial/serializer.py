from rest_framework import serializers
from .models import Tutorial, ContentType, Image, Video, Keyword
from user.models import UserProfile


class CRUDTutorialSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    author = serializers.CharField(required=False)
    publish_date = serializers.CharField(required=False)
    comments = serializers.CharField()
    content_type = serializers.CharField()
    keywords = serializers.ListField(required=False)
    images = serializers.ListField(required=False)
    videos = serializers.ListField(required=False)

    class Meta:
        model = Tutorial
        fields = '__all__'

    def create(self, validated_data):
        title = validated_data.get('title')
        description = validated_data.get('description')
        author = validated_data.get('author')
        if author:
            auth_obj = UserProfile.objects.get(uuid=author)
        publish_date = validated_data.get('publish_date')
        comments = validated_data.get('comments')
        content_type = validated_data.get('content_type')
        if content_type:
            content_obj = ContentType.objects.get(id=content_type)

        tutorial = Tutorial.objects.create(title=title, description=description, author=auth_obj,
                                           publish_date=publish_date,
                                           comments=comments, content_type=content_obj)
        keywords = validated_data.pop('keywords')
        for key in keywords:
            t_keyword = Keyword.objects.create(name=key['name'])
            tutorial.keywords.add(t_keyword)

        images = validated_data.pop('images')
        for img in images:
            t_image = Image.objects.create(title=img['title'], image_url=img['image_url'])
            tutorial.images.add(t_image)

        videos = validated_data.pop('videos')
        for video in videos:
            t_video = Video.objects.create(title=video['title'], video_url=video['video_url'])
            tutorial.videos.add(t_video)

        return tutorial


class TutorialUpdateSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    comments = serializers.CharField()
    content_type = serializers.CharField(required=False)
    keywords = serializers.ListField(required=False)
    images = serializers.ListField(required=False)
    videos = serializers.ListField(required=False)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.comments = validated_data.get('comments')
        con_obj = ContentType.objects.get(id=validated_data.pop('content_type'))
        if con_obj:
            instance.content_type = con_obj
            instance.save()
        else:
            instance.content_type = con_obj
            instance.save()

        tutorial = Tutorial.objects.get(uuid=instance.uuid)
        old_key = tutorial.keywords.filter()
        if not validated_data["keywords"]:
            for okey in old_key:
                key = Keyword.objects.filter(name=okey.name)
                key.delete()

        for okey in old_key:
            for key_data in validated_data["keywords"]:
                print(
                    "key_data.id-------------->",
                    key_data["name"],
                )
                key = Keyword.objects.filter(name=okey.name)
                key.delete()

        for exp_data in validated_data["keywords"]:
            tutorial_key = Keyword.objects.create(name=exp_data['name'])
            instance.keywords.add(tutorial_key)

        old_img = tutorial.images.filter()
        if not validated_data["images"]:
            for oimg in old_img:
                # instance.images.remove(oimg)
                img = Image.objects.filter(image_url=oimg.image_url)
                img.delete()
                print("images deleted")

        for oimg in old_img:
            for img_data in validated_data["images"]:
                print(
                    "img_data.id-------------->",
                    img_data["image_url"],
                )
                img = Image.objects.filter(image_url=oimg.image_url)
                img.delete()

        for exp_data in validated_data["images"]:
            tutorial_image = Image.objects.create(title=exp_data['title'], image_url=exp_data['image_url'])
            instance.images.add(tutorial_image)

        old_video = tutorial.videos.filter()
        if not validated_data["videos"]:
            for ovideo in old_video:
                # instance.images.remove(oimg)
                video = Video.objects.filter(image_url=ovideo.video_url)
                video.delete()
                print("video deleted")

        for ovideo in old_video:
            for video_data in validated_data["videos"]:
                print(
                    "img_data.id-------------->",
                    video_data["video_url"],
                )
                video = Video.objects.filter(video_url=ovideo.video_url)
                video.delete()

        for exp_data in validated_data["videos"]:
            tutorial_videos = Video.objects.create(title=exp_data['title'], video_url=exp_data['video_url'])
            instance.videos.add(tutorial_videos)

        instance.save()
        return instance


class KeywordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyword
        fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class TutorialListSerializer(serializers.ModelSerializer):
    keywords = KeywordSerializer(many=True)
    images = ImageSerializer(many=True)
    videos = VideoSerializer(many=True)
    content_type = ContentTypeSerializer()
    author = UserProfileSerializer()

    class Meta:
        model = Tutorial
        fields = ['uuid', 'title', 'description', 'publish_date', 'comments',
                  'keywords', 'images', 'videos', 'content_type', 'author']
