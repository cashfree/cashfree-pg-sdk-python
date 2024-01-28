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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from cashfree_pg.models.saved_instrument_meta import SavedInstrumentMeta

class InstrumentEntity(BaseModel):
    """
    Saved card instrument object
    """
    customer_id: Optional[StrictStr] = Field(None, description="customer_id for which the instrument was saved")
    afa_reference: Optional[StrictStr] = Field(None, description="cf_payment_id of the successful transaction done while saving instrument")
    instrument_id: Optional[StrictStr] = Field(None, description="saved instrument id")
    instrument_type: Optional[StrictStr] = Field(None, description="Type of the saved instrument")
    instrument_uid: Optional[StrictStr] = Field(None, description="Unique id for the saved instrument")
    instrument_display: Optional[StrictStr] = Field(None, description="masked card number displayed to the customer")
    instrument_status: Optional[StrictStr] = Field(None, description="Status of the saved instrument.")
    created_at: Optional[StrictStr] = Field(None, description="Timestamp at which instrument was saved.")
    instrument_meta: Optional[SavedInstrumentMeta] = None
    __properties = ["customer_id", "afa_reference", "instrument_id", "instrument_type", "instrument_uid", "instrument_display", "instrument_status", "created_at", "instrument_meta"]

    @validator('instrument_type')
    def instrument_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('card'):
            raise ValueError("must be one of enum values ('card')")
        return value

    @validator('instrument_status')
    def instrument_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ACTIVE', 'INACTIVE'):
            raise ValueError("must be one of enum values ('ACTIVE', 'INACTIVE')")
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
    def from_json(cls, json_str: str) -> InstrumentEntity:
        """Create an instance of InstrumentEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> InstrumentEntity:
        """Create an instance of InstrumentEntity from a JSON string"""
        if "CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;customer_id&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getCustomerId&#39;, setter&#x3D;&#39;setCustomerId&#39;, description&#x3D;&#39;customer_id for which the instrument was saved&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;str&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;customer_id&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.customer_id;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;customer_id for which the instrument was saved&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;customer_id for which the instrument was saved&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;CustomerId&#39;, nameInSnakeCase&#x3D;&#39;CUSTOMER_ID&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;customer_id&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getCustomerId&#39;, setter&#x3D;&#39;setCustomerId&#39;, description&#x3D;&#39;customer_id for which the instrument was saved&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;str&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;customer_id&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.customer_id;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;customer_id for which the instrument was saved&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;customer_id for which the instrument was saved&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;CustomerId&#39;, nameInSnakeCase&#x3D;&#39;CUSTOMER_ID&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;customer_id&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getCustomerId&#39;, setter&#x3D;&#39;setCustomerId&#39;, description&#x3D;&#39;customer_id for which the instrument was saved&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;str&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;customer_id&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.customer_id;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;customer_id for which the instrument was saved&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;customer_id for which the instrument was saved&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;CustomerId&#39;, nameInSnakeCase&#x3D;&#39;CUSTOMER_ID&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;customer_id&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getCustomerId&#39;, setter&#x3D;&#39;setCustomerId&#39;, description&#x3D;&#39;customer_id for which the instrument was saved&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;str&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;customer_id&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.customer_id;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;customer_id for which the instrument was saved&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;customer_id for which the instrument was saved&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;CustomerId&#39;, nameInSnakeCase&#x3D;&#39;CUSTOMER_ID&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;customer_id&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getCustomerId&#39;, setter&#x3D;&#39;setCustomerId&#39;, description&#x3D;&#39;customer_id for which the instrument was saved&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;str&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;customer_id&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.customer_id;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;customer_id for which the instrument was saved&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;customer_id for which the instrument was saved&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;CustomerId&#39;, nameInSnakeCase&#x3D;&#39;CUSTOMER_ID&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;customer_id&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getCustomerId&#39;, setter&#x3D;&#39;setCustomerId&#39;, description&#x3D;&#39;customer_id for which the instrument was saved&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;str&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;customer_id&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.customer_id;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;customer_id for which the instrument was saved&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;customer_id for which the instrument was saved&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;CustomerId&#39;, nameInSnakeCase&#x3D;&#39;CUSTOMER_ID&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;customer_id&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getCustomerId&#39;, setter&#x3D;&#39;setCustomerId&#39;, description&#x3D;&#39;customer_id for which the instrument was saved&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;str&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;customer_id&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.customer_id;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;customer_id for which the instrument was saved&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;customer_id for which the instrument was saved&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;CustomerId&#39;, nameInSnakeCase&#x3D;&#39;CUSTOMER_ID&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;customer_id&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getCustomerId&#39;, setter&#x3D;&#39;setCustomerId&#39;, description&#x3D;&#39;customer_id for which the instrument was saved&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;str&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;customer_id&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.customer_id;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;customer_id for which the instrument was saved&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;customer_id for which the instrument was saved&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;CustomerId&#39;, nameInSnakeCase&#x3D;&#39;CUSTOMER_ID&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}""CodegenProperty{openApiType&#x3D;&#39;string&#39;, baseName&#x3D;&#39;customer_id&#39;, complexType&#x3D;&#39;null&#39;, getter&#x3D;&#39;getCustomerId&#39;, setter&#x3D;&#39;setCustomerId&#39;, description&#x3D;&#39;customer_id for which the instrument was saved&#39;, dataType&#x3D;&#39;str&#39;, datatypeWithEnum&#x3D;&#39;str&#39;, dataFormat&#x3D;&#39;null&#39;, name&#x3D;&#39;customer_id&#39;, min&#x3D;&#39;null&#39;, max&#x3D;&#39;null&#39;, defaultValue&#x3D;&#39;null&#39;, defaultValueWithParam&#x3D;&#39; &#x3D; data.customer_id;&#39;, baseType&#x3D;&#39;str&#39;, containerType&#x3D;&#39;null&#39;, containerTypeMapped&#x3D;&#39;null&#39;, title&#x3D;&#39;null&#39;, unescapedDescription&#x3D;&#39;customer_id for which the instrument was saved&#39;, maxLength&#x3D;null, minLength&#x3D;null, pattern&#x3D;&#39;null&#39;, example&#x3D;&#39;&#39;&#39;&#39;, jsonSchema&#x3D;&#39;{
  &quot;type&quot; : &quot;string&quot;,
  &quot;description&quot; : &quot;customer_id for which the instrument was saved&quot;
}&#39;, minimum&#x3D;&#39;null&#39;, maximum&#x3D;&#39;null&#39;, exclusiveMinimum&#x3D;false, exclusiveMaximum&#x3D;false, required&#x3D;false, deprecated&#x3D;false, hasMoreNonReadOnly&#x3D;false, isPrimitiveType&#x3D;true, isModel&#x3D;false, isContainer&#x3D;false, isString&#x3D;true, isNumeric&#x3D;false, isInteger&#x3D;false, isShort&#x3D;false, isLong&#x3D;false, isUnboundedInteger&#x3D;false, isNumber&#x3D;false, isFloat&#x3D;false, isDouble&#x3D;false, isDecimal&#x3D;false, isByteArray&#x3D;false, isBinary&#x3D;false, isFile&#x3D;false, isBoolean&#x3D;false, isDate&#x3D;false, isDateTime&#x3D;false, isUuid&#x3D;false, isUri&#x3D;false, isEmail&#x3D;false, isPassword&#x3D;false, isFreeFormObject&#x3D;false, isArray&#x3D;false, isMap&#x3D;false, isEnum&#x3D;false, isInnerEnum&#x3D;false, isEnumRef&#x3D;false, isAnyType&#x3D;false, isReadOnly&#x3D;false, isWriteOnly&#x3D;false, isNullable&#x3D;false, isSelfReference&#x3D;false, isCircularReference&#x3D;false, isDiscriminator&#x3D;false, isNew&#x3D;false, isOverridden&#x3D;null, _enum&#x3D;null, allowableValues&#x3D;null, items&#x3D;null, additionalProperties&#x3D;null, vars&#x3D;[], requiredVars&#x3D;[], mostInnerItems&#x3D;null, vendorExtensions&#x3D;{}, hasValidation&#x3D;false, isInherited&#x3D;false, discriminatorValue&#x3D;&#39;null&#39;, nameInCamelCase&#x3D;&#39;CustomerId&#39;, nameInSnakeCase&#x3D;&#39;CUSTOMER_ID&#39;, enumName&#x3D;&#39;null&#39;, maxItems&#x3D;null, minItems&#x3D;null, maxProperties&#x3D;null, minProperties&#x3D;null, uniqueItems&#x3D;false, uniqueItemsBoolean&#x3D;null, multipleOf&#x3D;null, isXmlAttribute&#x3D;false, xmlPrefix&#x3D;&#39;null&#39;, xmlName&#x3D;&#39;null&#39;, xmlNamespace&#x3D;&#39;null&#39;, isXmlWrapped&#x3D;false, isNull&#x3D;false, isVoid&#x3D;false, getAdditionalPropertiesIsAnyType&#x3D;false, getHasVars&#x3D;false, getHasRequired&#x3D;false, getHasDiscriminatorWithNonEmptyMapping&#x3D;false, composedSchemas&#x3D;null, hasMultipleTypes&#x3D;false, requiredVarsMap&#x3D;null, ref&#x3D;null, schemaIsFromAdditionalProperties&#x3D;false, isBooleanSchemaTrue&#x3D;false, isBooleanSchemaFalse&#x3D;false, format&#x3D;null, dependentRequired&#x3D;null, contains&#x3D;null}" not in json_str:
            return None
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of instrument_meta
        if self.instrument_meta:
            _dict['instrument_meta'] = self.instrument_meta.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InstrumentEntity:
        """Create an instance of InstrumentEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return InstrumentEntity.parse_obj(obj)

        _obj = InstrumentEntity.parse_obj({
            "customer_id": obj.get("customer_id"),
            "afa_reference": obj.get("afa_reference"),
            "instrument_id": obj.get("instrument_id"),
            "instrument_type": obj.get("instrument_type"),
            "instrument_uid": obj.get("instrument_uid"),
            "instrument_display": obj.get("instrument_display"),
            "instrument_status": obj.get("instrument_status"),
            "created_at": obj.get("created_at"),
            "instrument_meta": SavedInstrumentMeta.from_dict(obj.get("instrument_meta")) if obj.get("instrument_meta") is not None else None
        })
        return _obj


