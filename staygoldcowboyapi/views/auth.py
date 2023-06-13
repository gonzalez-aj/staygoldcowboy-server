from staygoldcowboyapi.models import Fan
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Fan

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    fan = Fan.objects.filter(uid=uid).first()

    if fan is not None:
        data = {
            'id': fan.id,
            'uid': fan.uid,
            'first_name': fan.first_name,
            'last_name': fan.last_name
        }
        return Response(data)
    else:
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new fan for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    fan = Fan.objects.create(
        uid=request.data['uid'],
        first_name=request.data['firstName'],
        last_name=request.data['lastName']
    )

    data = {
        'id': fan.id,
        'uid': fan.uid,
        'first_name': fan.first_name,
        'last_name': fan.last_name
    }
    return Response(data)
