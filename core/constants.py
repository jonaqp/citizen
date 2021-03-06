from django.utils.translation import ugettext_lazy as _

CODE_TEXT_EDIT = 'EDIT'
TEXT_MSG_SUCCESS = _('Data saved correctly')
TEXT_MSG_ERROR = _('There was an error saving information')
TEXT_MSG_WARNING = _('It required to complete required fields')
STATUS_MSG_TAGS = {
    'success': TEXT_MSG_SUCCESS,
    'error': TEXT_MSG_ERROR,
    'warning': TEXT_MSG_WARNING,
}

NAME_SELECT_DEFAULT = _('--Choose--')
SELECT_DEFAULT_ = [('', NAME_SELECT_DEFAULT)]
SELECT_DEFAULT = (('', NAME_SELECT_DEFAULT),)
DISABLED = 'DISABLED'
ENABLED = 'ENABLED'
STATUS_MODEL1 = (
    (ENABLED, _('Enabled')),
    (DISABLED, _('Disabled')),
)

# ITEMS IDENTITY DOCUMENT
CODE_DOCUMENT_DNI = 'DOC-1'
CODE_DOCUMENT_RUC = 'DOC-2'
CODE_DOCUMENT_PASSPORT = 'DOC-3'
SIS_DOCUMENT_DNI_STRING = (CODE_DOCUMENT_DNI, _('DNI'))
SIS_DOCUMENT_RUC_STRING = (CODE_DOCUMENT_RUC, _('RUC'))
SIS_DOCUMENT_PASSPORT_STRING = (CODE_DOCUMENT_PASSPORT, _('PASSPORT'))
TYPE_IDENTITY_DOCUMENT_OPTIONS = (
    SIS_DOCUMENT_DNI_STRING, SIS_DOCUMENT_RUC_STRING, SIS_DOCUMENT_PASSPORT_STRING
)

# ITEMS TRIBUTE PERSON
CODE_TRIBUTE_PERSON_NATURAL = 'PERS-1'
CODE_TRIBUTE_PERSON_JURIDICAL = 'PERS-2'
SIS_TRIBUTE_PERSON_NATURAL_STRING = (CODE_TRIBUTE_PERSON_NATURAL, _('Natural'))
SIS_TRIBUTE_PERSON_JURIDICAL_STRING = (CODE_TRIBUTE_PERSON_JURIDICAL, _('Legal'))

TRIBUTE_PERSON_OPTIONS = (
    SIS_TRIBUTE_PERSON_NATURAL_STRING, SIS_TRIBUTE_PERSON_JURIDICAL_STRING
)

# ITEMS GENDER
CODE_GENDER_MALE = 'GEN-1'
CODE_GENDER_FEMALE = 'GEN-2'
SIS_GENDER_MALE_STRING = (CODE_GENDER_MALE, _('Male'))
SIS_GENDER_FEMALE_STRING = (CODE_GENDER_FEMALE, _('Female'))
TYPE_GENDER_OPTIONS = (
    SIS_GENDER_MALE_STRING, SIS_GENDER_FEMALE_STRING
)

# ITEMS CIVIL STATUS
CODE_CIVIL_STATUS_SINGLE = 'CVS-1'
CODE_CIVIL_STATUS_MARRIED = 'CVS-2'
CODE_CIVIL_STATUS_WIDOWED = 'CVS-3'
CODE_CIVIL_STATUS_DIVORCED = 'CVS-4'
CODE_CIVIL_STATUS_SEPARATED = 'CVS-5'
SIS_CIVIL_STATUS_SINGLE_STRING = (CODE_CIVIL_STATUS_SINGLE, _('Single'))
SIS_CIVIL_STATUS_MARRIED_STRING = (CODE_CIVIL_STATUS_MARRIED, _('Married'))
SIS_CIVIL_STATUS_WIDOWED_STRING = (CODE_CIVIL_STATUS_WIDOWED, _('Widowed'))
SIS_CIVIL_STATUS_DIVORCED_STRING = (CODE_CIVIL_STATUS_DIVORCED, _('Divorced'))
SIS_CIVIL_STATUS_SEPARATED_STRING = (CODE_CIVIL_STATUS_SEPARATED, _('Separated'))
TYPE_CIVIL_STATUS_OPTIONS = (
    SIS_CIVIL_STATUS_SINGLE_STRING, SIS_CIVIL_STATUS_MARRIED_STRING, SIS_CIVIL_STATUS_WIDOWED_STRING,
    SIS_CIVIL_STATUS_DIVORCED_STRING, SIS_CIVIL_STATUS_SEPARATED_STRING
)

