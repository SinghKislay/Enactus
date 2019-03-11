from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework.serializers import(
    ModelSerializer,
    EmailField,
    CharField,
    HyperlinkedIdentityField,
    SerializerMethodField,
    ValidationError
)
from rest_framework.authtoken.models import Token
from customer.models import Customer,Service,Employee
User = get_user_model()

class UserCreateSerializer(ModelSerializer):
    email=EmailField()
    email2=EmailField(label='Confirm Email')
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'email2',
            'password',
               
        ]
        extra_kwargs={'password':
               {'write_only':True}
               }
    
    def create(self,validated_data):
        username=validated_data['username']
        email=validated_data['email']
        password=validated_data['password']
        user_obj=User(
            username=username,
            email=email,
        )
        customer_obj=Customer(username=username)
        customer_obj.save()
        service_obj=Service(username=username)
        service_obj.save()
        user_obj.set_password(password)
        user_obj.save()
        return validated_data

    def validate_email2(self,value):
        data=self.get_initial()
        email1=data.get('email')
        email2=value
        if email1!=email2:
            raise ValidationError('Emails must match')
        return value

    def validate(self,data):
        email=data['email']
        username=data['username']
        email_qs=User.objects.filter(email=email)
        username_qs=User.objects.filter(username=username)
        if email_qs.exists() or username_qs.exists():
            raise ValidationError("This user already exists")
        return data



class UserLoginSerializer(ModelSerializer):
    username=CharField(required=False,allow_blank=True)
    email=EmailField(label='Email',allow_blank=True,required=False)
    token=CharField(allow_blank=True,read_only=True)
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password',
            'token'
        ]
        
        extra_kwargs={'password':
               {'write_only':True}
               }
    
    def validate(self,data):
        email =data.get("email",None)
        username=data.get("username",None)
        password=data["password"]
        if not email and not username:
            raise ValidationError("A username or email is reqired to login")
        user =User.objects.filter(
            Q(email=email)|Q(username=username)
        ).distinct()
        #user=user.exclude(email_isnull=True).exclude(email_iexact='')
        if user.exists() and user.count() ==1:
            user_obj=user.first()
        else:
            raise ValidationError("This username/email not valid")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again")
        token,_=Token.objects.get_or_create(user=user_obj)
        data["token"]=token.key
        return data


class DataCatcherSerializer(ModelSerializer):
    name=CharField(required=True)
    location=CharField(required=True)
    class Meta:
        model=Customer
        fields=('username','location')

    def create(self,validated_data):
        name=validated_data['username']
        location=validated_data['location']
        customer_obj=Customer(
            username=name,location=location
        )
        customer_obj.save()
        return validated_data

    def validate(self,data):
        name=data['name']
        name_qs=Customer.objects.filter(name=name)
        
        if name_qs.exists():
            raise ValidationError("This user Alreay exists")
        return data
class DataUpdateSerializer(ModelSerializer):
    name=CharField(required=True)
    class Meta:
        model=Customer
        fileds=fields=[
            'username',
            'name',
            'location',
            'starting_time',
        ]
    
    def create(self,validated_data):
        print('ram1')
        username=validated_data['username']
        name=validated_data['name']
        location=validated_data['location']
        st=int(validated_data['starting_time'])
        customer_obj=Customer.objects.filter(username=username)
        customer_obj.update(name=name,location=location,starting_time=st)
        
        
        return validated_data

    def validate(self,data):
        name=data['username']
        name_qs=User.objects.filter(username=name)
        if not name_qs.exists():
            raise ValidationError("This user doesn't exists in the DB")
        return data

class ServiceSerializer(ModelSerializer):
    class Meta:
        model=Service
        fileds=fields='__all__'
    
    def validate(self,data):
        name=data['username']
        name_qs=User.objects.filter(username=name)
        if not name_qs.exists():
            raise ValidationError("This user doesn't exists in the DB")
        return data

    def create(self,validated_data):
        username=validated_data['username']
        date=validated_data['date']
        timeslot=validated_data['timeslot']
        worktime=validated_data['worktime']
        service_obj=Service.objects.filter(username=username)
        service_obj.update(date=date,timeslot=timeslot,worktime=worktime)
        return validated_data

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fileds=fields=['username','working']

    def validate(self,data):
        name=data['username']
        name_qs=Employee.objects.filter(username=name)
        if not name_qs.exists():
            raise ValidationError("This user doesn't exists in the DB")
        return data

    def create(self,validated_data):
        username=validated_data['username']
        working=validated_data['working']
        service_obj=Employee.objects.filter(username=username)
        service_obj.update(working=working)
        return validated_data



    

