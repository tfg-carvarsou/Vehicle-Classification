/* generated using openapi-typescript-codegen -- do not edit */
/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { VCImageGet } from '../models/VCImageGet';
import type { VCImagePost } from '../models/VCImagePost';
import type { VCImagePostRequest } from '../models/VCImagePostRequest';
import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';
export class ClassifierService {
    /**
     * Retrieve an image by its code
     * @param code
     * @returns VCImageGet The image has been retrieved successfully
     * @throws ApiError
     */
    public static classifierSnapviewRetrieve(
        code: string,
    ): CancelablePromise<VCImageGet> {
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
     * @returns VCImageGet The images has been listed successfully
     * @throws ApiError
     */
    public static classifierSnapzoneList(): CancelablePromise<Array<VCImageGet>> {
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
     * @returns VCImagePost The image has been uploaded successfully
     * @throws ApiError
     */
    public static classifierSnapzoneCreate(
        formData: VCImagePostRequest,
    ): CancelablePromise<VCImagePost> {
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
