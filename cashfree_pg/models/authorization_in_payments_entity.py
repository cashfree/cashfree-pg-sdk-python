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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class AuthorizationInPaymentsEntity(BaseModel):
    """
    If preauth enabled for account you will get this body
    """
    action: Optional[StrictStr] = Field(None, description="One of CAPTURE or VOID")
    status: Optional[StrictStr] = Field(None, description="One of SUCCESS or PENDING")
    captured_amount: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The captured amount for this authorization request")
    start_time: Optional[StrictStr] = Field(None, description="Start time of this authorization hold (only for UPI)")
    end_time: Optional[StrictStr] = Field(None, description="End time of this authorization hold (only for UPI)")
    approve_by: Optional[StrictStr] = Field(None, description="Approve by time as passed in the authorization request (only for UPI)")
    action_reference: Optional[StrictStr] = Field(None, description="CAPTURE or VOID reference number based on action ")
    action_time: Optional[StrictStr] = Field(None, description="Time of action (CAPTURE or VOID)")
    __properties = ["action", "status", "captured_amount", "start_time", "end_time", "approve_by", "action_reference", "action_time"]

    @validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('CAPTURE', 'VOID'):
            raise ValueError("must be one of enum values ('CAPTURE', 'VOID')")
        return value

    @validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('SUCCESS', 'PENDING'):
            raise ValueError("must be one of enum values ('SUCCESS', 'PENDING')")
        return value

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
    def from_json(cls, json_str: str) -> AuthorizationInPaymentsEntity:
        """Create an instance of AuthorizationInPaymentsEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> AuthorizationInPaymentsEntity:
        """Create an instance of AuthorizationInPaymentsEntity from a JSON string"""
        if "CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;action&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getAction&#39;, setter&#x3D;&#39;setAction&#39;, description&#x3D;&#39;One of CAPTURE or VOID&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;ActionEnum&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;action&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.action;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;One of CAPTURE or VOID&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;CAPTURE&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;One of CAPTURE or VOID&quot;,
  &quot;enum&quot; : [ &quot;CAPTURE&quot;, &quot;VOID&quot; ]
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;true, isInnerEnum&#x3D;true, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;[CAPTURE, VOID], allowableValues&#x3D;{enumVars&#x3D;[{name&#x3D;&#39;CAPTURE&#39;, isString&#x3D;true, value&#x3D;&#39;CAPTURE&#39;}, {name&#x3D;&#39;VOID&#39;, isString&#x3D;true, value&#x3D;&#39;VOID&#39;}], values&#x3D;[CAPTURE, VOID]}, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;Action&#39;, nameInSnakeCase&#x3D;&#39;ACTION&#39;, enumName&#x3D;&#39;ActionEnum&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;action&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getAction&#39;, setter&#x3D;&#39;setAction&#39;, description&#x3D;&#39;One of CAPTURE or VOID&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;ActionEnum&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;action&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.action;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;One of CAPTURE or VOID&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;CAPTURE&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;One of CAPTURE or VOID&quot;,
  &quot;enum&quot; : [ &quot;CAPTURE&quot;, &quot;VOID&quot; ]
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;true, isInnerEnum&#x3D;true, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;[CAPTURE, VOID], allowableValues&#x3D;{enumVars&#x3D;[{name&#x3D;&#39;CAPTURE&#39;, isString&#x3D;true, value&#x3D;&#39;CAPTURE&#39;}, {name&#x3D;&#39;VOID&#39;, isString&#x3D;true, value&#x3D;&#39;VOID&#39;}], values&#x3D;[CAPTURE, VOID]}, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;Action&#39;, nameInSnakeCase&#x3D;&#39;ACTION&#39;, enumName&#x3D;&#39;ActionEnum&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;action&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getAction&#39;, setter&#x3D;&#39;setAction&#39;, description&#x3D;&#39;One of CAPTURE or VOID&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;ActionEnum&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;action&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.action;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;One of CAPTURE or VOID&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;CAPTURE&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;One of CAPTURE or VOID&quot;,
  &quot;enum&quot; : [ &quot;CAPTURE&quot;, &quot;VOID&quot; ]
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;true, isInnerEnum&#x3D;true, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;[CAPTURE, VOID], allowableValues&#x3D;{enumVars&#x3D;[{name&#x3D;&#39;CAPTURE&#39;, isString&#x3D;true, value&#x3D;&#39;CAPTURE&#39;}, {name&#x3D;&#39;VOID&#39;, isString&#x3D;true, value&#x3D;&#39;VOID&#39;}], values&#x3D;[CAPTURE, VOID]}, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;Action&#39;, nameInSnakeCase&#x3D;&#39;ACTION&#39;, enumName&#x3D;&#39;ActionEnum&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;action&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getAction&#39;, setter&#x3D;&#39;setAction&#39;, description&#x3D;&#39;One of CAPTURE or VOID&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;ActionEnum&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;action&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.action;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;One of CAPTURE or VOID&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;CAPTURE&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;One of CAPTURE or VOID&quot;,
  &quot;enum&quot; : [ &quot;CAPTURE&quot;, &quot;VOID&quot; ]
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;true, isInnerEnum&#x3D;true, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;[CAPTURE, VOID], allowableValues&#x3D;{enumVars&#x3D;[{name&#x3D;&#39;CAPTURE&#39;, isString&#x3D;true, value&#x3D;&#39;CAPTURE&#39;}, {name&#x3D;&#39;VOID&#39;, isString&#x3D;true, value&#x3D;&#39;VOID&#39;}], values&#x3D;[CAPTURE, VOID]}, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;Action&#39;, nameInSnakeCase&#x3D;&#39;ACTION&#39;, enumName&#x3D;&#39;ActionEnum&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;action&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getAction&#39;, setter&#x3D;&#39;setAction&#39;, description&#x3D;&#39;One of CAPTURE or VOID&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;ActionEnum&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;action&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.action;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;One of CAPTURE or VOID&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;CAPTURE&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;One of CAPTURE or VOID&quot;,
  &quot;enum&quot; : [ &quot;CAPTURE&quot;, &quot;VOID&quot; ]
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;true, isInnerEnum&#x3D;true, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;[CAPTURE, VOID], allowableValues&#x3D;{enumVars&#x3D;[{name&#x3D;&#39;CAPTURE&#39;, isString&#x3D;true, value&#x3D;&#39;CAPTURE&#39;}, {name&#x3D;&#39;VOID&#39;, isString&#x3D;true, value&#x3D;&#39;VOID&#39;}], values&#x3D;[CAPTURE, VOID]}, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;Action&#39;, nameInSnakeCase&#x3D;&#39;ACTION&#39;, enumName&#x3D;&#39;ActionEnum&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;action&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getAction&#39;, setter&#x3D;&#39;setAction&#39;, description&#x3D;&#39;One of CAPTURE or VOID&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;ActionEnum&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;action&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.action;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;One of CAPTURE or VOID&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;CAPTURE&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;One of CAPTURE or VOID&quot;,
  &quot;enum&quot; : [ &quot;CAPTURE&quot;, &quot;VOID&quot; ]
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;true, isInnerEnum&#x3D;true, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;[CAPTURE, VOID], allowableValues&#x3D;{enumVars&#x3D;[{name&#x3D;&#39;CAPTURE&#39;, isString&#x3D;true, value&#x3D;&#39;CAPTURE&#39;}, {name&#x3D;&#39;VOID&#39;, isString&#x3D;true, value&#x3D;&#39;VOID&#39;}], values&#x3D;[CAPTURE, VOID]}, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;Action&#39;, nameInSnakeCase&#x3D;&#39;ACTION&#39;, enumName&#x3D;&#39;ActionEnum&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;action&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getAction&#39;, setter&#x3D;&#39;setAction&#39;, description&#x3D;&#39;One of CAPTURE or VOID&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;ActionEnum&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;action&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.action;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;One of CAPTURE or VOID&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;CAPTURE&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;One of CAPTURE or VOID&quot;,
  &quot;enum&quot; : [ &quot;CAPTURE&quot;, &quot;VOID&quot; ]
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;true, isInnerEnum&#x3D;true, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;[CAPTURE, VOID], allowableValues&#x3D;{enumVars&#x3D;[{name&#x3D;&#39;CAPTURE&#39;, isString&#x3D;true, value&#x3D;&#39;CAPTURE&#39;}, {name&#x3D;&#39;VOID&#39;, isString&#x3D;true, value&#x3D;&#39;VOID&#39;}], values&#x3D;[CAPTURE, VOID]}, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;Action&#39;, nameInSnakeCase&#x3D;&#39;ACTION&#39;, enumName&#x3D;&#39;ActionEnum&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;action&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getAction&#39;, setter&#x3D;&#39;setAction&#39;, description&#x3D;&#39;One of CAPTURE or VOID&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;ActionEnum&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;action&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.action;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;One of CAPTURE or VOID&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;CAPTURE&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;One of CAPTURE or VOID&quot;,
  &quot;enum&quot; : [ &quot;CAPTURE&quot;, &quot;VOID&quot; ]
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;true, isInnerEnum&#x3D;true, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;[CAPTURE, VOID], allowableValues&#x3D;{enumVars&#x3D;[{name&#x3D;&#39;CAPTURE&#39;, isString&#x3D;true, value&#x3D;&#39;CAPTURE&#39;}, {name&#x3D;&#39;VOID&#39;, isString&#x3D;true, value&#x3D;&#39;VOID&#39;}], values&#x3D;[CAPTURE, VOID]}, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;Action&#39;, nameInSnakeCase&#x3D;&#39;ACTION&#39;, enumName&#x3D;&#39;ActionEnum&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AuthorizationInPaymentsEntity:
        """Create an instance of AuthorizationInPaymentsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AuthorizationInPaymentsEntity.parse_obj(obj)

        _obj = AuthorizationInPaymentsEntity.parse_obj({
            "action": obj.get("action"),
            "status": obj.get("status"),
            "captured_amount": obj.get("captured_amount"),
            "start_time": obj.get("start_time"),
            "end_time": obj.get("end_time"),
            "approve_by": obj.get("approve_by"),
            "action_reference": obj.get("action_reference"),
            "action_time": obj.get("action_time")
        })
        return _obj


