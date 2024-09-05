/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VCImage } from '../models/VCImage';
import type { VCImageRequest } from '../models/VCImageRequest';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ClassifierService {
    /**
     * Retrieve an image by its code
     * @param code
     * @returns VCImage The image has been retrieved successfully
     * @throws ApiError
     */
    public static classifierSnapviewRetrieve(
        code: string,
    ): CancelablePromise<VCImage> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/classifier/snapview/{code}/',
            path: {
                'code': code,
            },
            errors: {
                400: `There has been an incident when retrieving the image. Please try again`,
                404: `The image does not exist`,
            },
        });
    }
    /**
     * Delete an image by its code
     * @param code
     * @returns void
     * @throws ApiError
     */
    public static classifierSnapviewDestroy(
        code: string,
    ): CancelablePromise<void> {
        return __request(OpenAPI, {
            method: 'DELETE',
            url: '/classifier/snapview/{code}/',
            path: {
                'code': code,
            },
            errors: {
                400: `There has been an incident when deleting the image. Please try again`,
                404: `The image does not exist`,
            },
        });
    }
    /**
     * List all images
     * @returns VCImage The images has been listed successfully
     * @throws ApiError
     */
    public static classifierSnapzoneList(): CancelablePromise<Array<VCImage>> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/classifier/snapzone/',
            errors: {
                400: `There has been an incident when listing the images. Please try again`,
            },
        });
    }
    /**
     * Upload an image to classify vehicles
     * @param formData
     * @returns VCImage The image has been uploaded successfully
     * @throws ApiError
     */
    public static classifierSnapzoneCreate(
        formData: VCImageRequest,
    ): CancelablePromise<VCImage> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/classifier/snapzone/',
            formData: formData,
            mediaType: 'multipart/form-data',
            errors: {
                400: `There has been an incident when uploading the image. Please try again`,
            },
        });
    }
}
