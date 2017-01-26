# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import v1.atomic_elements.atoms
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import v1.blocks
import v1.atomic_elements.organisms


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0049_remove_main_contact_info_from_sidefoot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='browsepage',
            name='content',
            field=wagtail.wagtailcore.fields.StreamField([(b'bureau_structure', wagtail.wagtailcore.blocks.StructBlock([(b'last_updated_date', wagtail.wagtailcore.blocks.DateBlock(required=False)), (b'download_image', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon=b'image')), (b'director', wagtail.wagtailcore.blocks.CharBlock()), (b'divisions', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'division', v1.blocks.PlaceholderCharBlock(label=b'Division')), (b'division_lead', v1.blocks.PlaceholderCharBlock(placeholder=b'Name')), (b'title', wagtail.wagtailcore.blocks.StructBlock([(b'line_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 1')), (b'line_2', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 2'))])), (b'link_to_division_page', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'offices', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'office_name', wagtail.wagtailcore.blocks.CharBlock()), (b'lead', v1.blocks.PlaceholderCharBlock(placeholder=b'Name')), (b'title', wagtail.wagtailcore.blocks.StructBlock([(b'line_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 1')), (b'line_2', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 2'))]))], required=False)))]))), (b'office_of_the_director', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'office_name', wagtail.wagtailcore.blocks.CharBlock()), (b'lead', v1.blocks.PlaceholderCharBlock(placeholder=b'Name')), (b'title', wagtail.wagtailcore.blocks.StructBlock([(b'line_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 1')), (b'line_2', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 2'))])), (b'offices', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'office_name', wagtail.wagtailcore.blocks.CharBlock()), (b'lead', v1.blocks.PlaceholderCharBlock(placeholder=b'Name')), (b'title', wagtail.wagtailcore.blocks.StructBlock([(b'line_1', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 1')), (b'line_2', v1.blocks.PlaceholderCharBlock(required=False, placeholder=b'Title 2'))]))], required=False)))]), label=b'Office of the Director'))])), (b'image_text_25_75_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'should_link_image', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b"Check this to link all images to the URL of the first link in their unit's list, if there is a link.", default=False, required=False)), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False))])))])), (b'image_text_50_50_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'sharing', wagtail.wagtailcore.blocks.StructBlock([(b'shareable', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'If checked, share links will be included below the items.', required=False, label=b'Include sharing links?')), (b'share_blurb', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Sets the tweet text, email subject line, and LinkedIn post text.', required=False))])), (b'image_texts', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'is_widescreen', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Use 16:9 image')), (b'is_button', wagtail.wagtailcore.blocks.BooleanBlock(required=False, label=b'Show links as button')), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'half_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'has_top_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_bottom_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H3 heading')), (b'sub_heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H4 heading')), (b'sub_heading_icon', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A list of icon names can be obtained at: https://cfpb.github.io/capital-framework/components/cf-icons/. Examples: linkedin-square, facebook-square, etc.', required=False, label=b'H4 heading icon')), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'third_width_link_blob_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, icon=b'title')), (b'has_top_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_bottom_border', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'link_blobs', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H3 heading')), (b'sub_heading', wagtail.wagtailcore.blocks.CharBlock(required=False, label=b'H4 heading')), (b'sub_heading_icon', wagtail.wagtailcore.blocks.CharBlock(help_text=b'A list of icon names can be obtained at: https://cfpb.github.io/capital-framework/components/cf-icons/. Examples: linkedin-square, facebook-square, etc.', required=False, label=b'H4 heading icon')), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False, blank=True)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]), required=False))])))])), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'full_width_text', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=(b'Auto-generated on save, or enter some human-friendly text ', b'to make it easier to read.'), required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'}))])), (b'expandable', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'links', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])), (b'expandable_group', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'is_accordion', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'has_rule', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'expandables', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'is_bordered', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_midtone', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'is_expanded', wagtail.wagtailcore.blocks.BooleanBlock(required=False)), (b'content', wagtail.wagtailcore.blocks.StreamBlock([(b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'well', wagtail.wagtailcore.blocks.StructBlock([(b'content', wagtail.wagtailcore.blocks.RichTextBlock(required=False, label=b'Well'))])), (b'links', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'email', wagtail.wagtailcore.blocks.StructBlock([(b'emails', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'phone', wagtail.wagtailcore.blocks.StructBlock([(b'fax', wagtail.wagtailcore.blocks.BooleanBlock(default=False, required=False, label=b'Is this number a fax?')), (b'phones', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'number', wagtail.wagtailcore.blocks.CharBlock(max_length=15)), (b'vanity', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False)), (b'tty', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))])))])), (b'address', wagtail.wagtailcore.blocks.StructBlock([(b'label', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'title', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'street', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'city', wagtail.wagtailcore.blocks.CharBlock(max_length=50, required=False)), (b'state', wagtail.wagtailcore.blocks.CharBlock(max_length=25, required=False)), (b'zip_code', wagtail.wagtailcore.blocks.CharBlock(max_length=15, required=False))]))], blank=True))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'})), (b'job_listing_table', wagtail.wagtailcore.blocks.StructBlock([(b'first_row_is_table_header', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the first row as a header.', default=True, required=False)), (b'first_col_is_header', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the first column as a header.', default=False, required=False)), (b'is_full_width', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the table at full width.', default=False, required=False)), (b'is_striped', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Display the table with striped rows.', default=False, required=False)), (b'is_stacked', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Stack the table columns on mobile.', default=True, required=False)), (b'empty_table_msg', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Message to display if there is no table data.', required=False, label=b'No Table Data Message')), (b'hide_closed', wagtail.wagtailcore.blocks.BooleanBlock(help_text=b'Whether to hide jobs that are not currently open (jobs will automatically update)', default=True, required=False))])), (b'feedback', wagtail.wagtailcore.blocks.StructBlock([(b'was_it_helpful_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Use this field only for feedback forms that use "Was this helpful?" radio buttons.', default=b'Was this page helpful to you?', required=False)), (b'intro_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional feedback intro', required=False)), (b'question_text', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional expansion on intro', required=False)), (b'radio_intro', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Leave blank unless you are building a feedback form with extra radio-button prompts, as in /owning-a-home/help-us-improve/.', required=False)), (b'radio_text', wagtail.wagtailcore.blocks.CharBlock(default=b'This information helps us understand your question better.', required=False)), (b'radio_question_1', wagtail.wagtailcore.blocks.CharBlock(default=b'How soon do you expect to buy a home?', required=False)), (b'radio_question_2', wagtail.wagtailcore.blocks.CharBlock(default=b'Do you currently own a home?', required=False)), (b'button_text', wagtail.wagtailcore.blocks.CharBlock(default=b'Submit')), (b'contact_advisory', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Use only for feedback forms that ask for a contact email', required=False))])), (b'conference_registration_form', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Note: Additional form field options will appear in Preview and Publish modes.', required=False)), (b'code', wagtail.wagtailcore.blocks.CharBlock(label=b'GovDelivery Code')), (b'sessions', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label=b'Session'), label=b'Sessions attending')), (b'capacity', v1.atomic_elements.atoms.IntegerBlock(help_text=b'Enter an integer that will be the conference attendance limit.')), (b'success_message', wagtail.wagtailcore.blocks.RichTextBlock(help_text=b'Enter a message that will be shown on successful registration.')), (b'at_capacity_message', wagtail.wagtailcore.blocks.StreamBlock([(b'content_with_anchor', wagtail.wagtailcore.blocks.StructBlock([(b'content_block', wagtail.wagtailcore.blocks.RichTextBlock()), (b'anchor_link', wagtail.wagtailcore.blocks.StructBlock([(b'link_id', wagtail.wagtailcore.blocks.CharBlock(help_text=(b'Auto-generated on save, or enter some human-friendly text ', b'to make it easier to read.'), required=False, label=b'ID for this content block'))]))])), (b'content', wagtail.wagtailcore.blocks.RichTextBlock(icon=b'edit')), (b'media', wagtail.wagtailimages.blocks.ImageChooserBlock(icon=b'image')), (b'quote', wagtail.wagtailcore.blocks.StructBlock([(b'body', wagtail.wagtailcore.blocks.TextBlock()), (b'citation', wagtail.wagtailcore.blocks.TextBlock())])), (b'cta', wagtail.wagtailcore.blocks.StructBlock([(b'slug_text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph_text', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'button', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))]))])), (b'related_links', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'links', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])))])), (b'table', wagtail.wagtailcore.blocks.StructBlock([(b'headers', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock())), (b'rows', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StreamBlock([(b'hyperlink', wagtail.wagtailcore.blocks.StructBlock([(b'text', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'url', wagtail.wagtailcore.blocks.CharBlock(default=b'/', required=False))])), (b'text', wagtail.wagtailcore.blocks.CharBlock()), (b'text_blob', wagtail.wagtailcore.blocks.TextBlock()), (b'rich_text_blob', wagtail.wagtailcore.blocks.RichTextBlock())])))], editable=False)), (b'table_block', v1.atomic_elements.organisms.AtomicTableBlock(table_options={b'renderer': b'html'}))], help_text=b'Enter a message that will be shown when the event is at capacity.')), (b'failure_message', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Enter a message that will be shown if the GovDelivery subscription fails.'))])), (b'html_block', wagtail.wagtailcore.blocks.StructBlock([(b'html_url', wagtail.wagtailcore.blocks.RegexBlock(regex=b'^https://(s3.amazonaws.com/)?files.consumerfinance.gov/.+$', default=b'', required=True, error_messages={b'required': b'The HTML URL field is required for rendering raw HTML from a remote source.', b'invalid': b'The URL is invalid or not allowed. '}, label=b'Source URL'))])), (b'chart_block', wagtail.wagtailcore.blocks.StructBlock([(b'title', wagtail.wagtailcore.blocks.CharBlock(required=True)), (b'chart_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'bar', b'Bar'), (b'line', b'Line'), (b'tile_map', b'Tile Map')])), (b'color_scheme', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b"Chart's color scheme. See https://github.com/cfpb/cfpb-chart-builder#configuration.", required=False, choices=[(b'green', b'Green'), (b'blue', b'Blue'), (b'teal', b'Teal'), (b'navy', b'Navy')])), (b'data_source', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Location of the chart\'s data source relative to "http://files.consumerfinance.gov/data/". For example,"consumer-credit-trends/volume_data_Score_Level_AUT.csv".', required=True)), (b'description', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Briefly summarize the chart for visually impaired users.', required=True)), (b'metadata', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Optional metadata for the chart to use. For example, with CCT this would be the chart\'s "group".', required=False)), (b'note', wagtail.wagtailcore.blocks.CharBlock(help_text=b'Text to display as a footnote. For example, "Data from the last six months are not final."', required=False))])), (b'snippet_list', wagtail.wagtailcore.blocks.StructBlock([(b'heading', wagtail.wagtailcore.blocks.CharBlock(required=False)), (b'body', wagtail.wagtailcore.blocks.RichTextBlock(required=False)), (b'image', wagtail.wagtailcore.blocks.StructBlock([(b'upload', wagtail.wagtailimages.blocks.ImageChooserBlock(required=False)), (b'alt', wagtail.wagtailcore.blocks.CharBlock(required=False))])), (b'snippet_type', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[(b'v1.models.snippets.Contact', 'Contacts'), (b'v1.models.snippets.Resource', 'Resources')])), (b'actions', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.StructBlock([(b'link_label', wagtail.wagtailcore.blocks.CharBlock(help_text=b'E.g., "Download" or "Order free prints"')), (b'snippet_field', wagtail.wagtailcore.blocks.ChoiceBlock(help_text=b'Corresponds to the available fields for the selectedsnippet type.', choices=[('Contacts', []), ('Resources', [(b'related_file', b'Related file'), (b'alternate_file', b'Alternate file'), (b'link', b'Link'), (b'alternate_link', b'Alternate link')])]))]))), (b'tags', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.CharBlock(label=b'Tag'), help_text=b'Enter tag names to filter the snippets. For a snippet to match and be output in the list, it must have been tagged with all of the tag names listed here. The tag names are case-insensitive.'))]))], blank=True),
        ),
    ]
