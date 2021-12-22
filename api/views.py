from category_encoders import OrdinalEncoder
from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response


class ChocoPrediction(APIView):
    def post(self, request):
        data = request.data
        encoder = OrdinalEncoder()
        encoder_data = encoder.fit_transform(data)
        company = encoder_data['company']
        specific_bean_origin = encoder_data['specific_bean_origin_or_bar_name']
        review_date =encoder_data['review_date']
        cocoa_percent =encoder_data['cocoa_percent']
        company_location = encoder_data['company_location']
        bean_type =encoder_data['Bean_Type']
        country = encoder_data['country_of_bean_origin']
        trinitario_bean =encoder_data['trinitario_bean']
        criollo_bean =encoder_data['criollo_bean']
        blend_bean = encoder_data['blend_bean']
        forastero_bean = encoder_data['forastero_bean']
        gbm_model = ApiConfig.model
        rating_predicted = gbm_model.predict([company,specific_bean_origin,review_date,
                                              cocoa_percent,company_location,bean_type,
                                              country,trinitario_bean,criollo_bean,blend_bean,
                                            forastero_bean])[0][0][0][0][0][0][0][0][0][0][0]
        response_dict ={"Predicted Rating": rating_predicted }
        return Response(response_dict, status=200)
