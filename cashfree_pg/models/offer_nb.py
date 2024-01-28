# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2022-09-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json



from pydantic import BaseModel, Field
from cashfree_pg.models.offer_nb_netbanking import OfferNBNetbanking

class OfferNB(BaseModel):
    """
    Offer object ofr NetBanking
    """
    netbanking: OfferNBNetbanking = Field(...)
    __properties = ["netbanking"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> OfferNB:
        """Create an instance of OfferNB from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> OfferNB:
        """Create an instance of OfferNB from a JSON string"""
        if "CodegenProperty{openApiType&#x3D;&#39;OfferNBNetbanking&#39;, baseName&#x3D;&#39;netbanking&#39;, complexType&#x3D;&#39;OfferNBNetbanking&#39;, getter&#x3D;&#39;getNetbanking&#39;, setter&#x3D;&#39;setNetbanking&#39;, description&#x3D;&#39;null&#39;, dataType&#x3D;&#39;OfferNBNetbanking&#39;, datatypeWithEnum&#x3D;&#39;OfferNBNetbanking&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;netbanking&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.netbanking;&#39;, baseType&#x3D;&#39;OfferNBNetbanking&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;null&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;cashfree_pg.models.offer_nb_netbanking.OfferNB_netbanking(
                    bank_name &#x3D; &#39;all&#39;, )&#39;, jsonSchema&#x3D;&#39;{
  &quot;$ref&quot; : &quot;#/components/schemas/OfferNB_netbanking&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;true, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;false, isModel&#x3D;true, isContainer&#x3D;false, isString&#x3D;false, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;Netbanking&#39;, nameInSnakeCase&#x3D;&#39;NETBANKING&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;#/components/schemas/OfferNB_netbanking, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of netbanking
        if self.netbanking:
            _dict['netbanking'] = self.netbanking.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferNB:
        """Create an instance of OfferNB from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferNB.parse_obj(obj)

        _obj = OfferNB.parse_obj({
            "netbanking": OfferNBNetbanking.from_dict(obj.get("netbanking")) if obj.get("netbanking") is not None else None
        })
        return _obj


